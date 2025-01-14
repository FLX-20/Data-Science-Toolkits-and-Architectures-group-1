import os
import uuid
import shutil
import keras
from PIL import Image
import tensorflow as tf
import numpy as np
from db_operations import split_data_into_training_and_testing, insert_image_metadata, create_connection, split_data_into_training_and_testing
from app_config import DATASET_PATH, DATASET_NAME


def download_data():

    final_dir = os.path.join(DATASET_PATH, DATASET_NAME)

    if os.path.exists(final_dir):
        print(f"The dataset '{
              DATASET_NAME}' already exists. Skipping download.")
        return

    tmp_dir = os.path.join(DATASET_PATH, "tmp")

    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    x_data = np.concatenate((x_train, x_test), axis=0)
    y_data = np.concatenate((y_train, y_test), axis=0)

    for idx, (image, label) in enumerate(zip(x_data, y_data)):
        label_folder = os.path.join(tmp_dir, str(label))
        os.makedirs(label_folder, exist_ok=True)

        image_path = os.path.join(label_folder, f"{idx}.jpg")
        img = Image.fromarray(image)
        img.save(image_path)

    print(f"Data successfully downloaded and saved in '{tmp_dir}'.")

    process_and_store_files(tmp_dir, final_dir)
    print("Data successfully processed and stored in the database.")

    split_data_into_training_and_testing()
    print("Data successfully split into training and testing with balanced classes.")

    clean_up(tmp_dir)
    print("Temporary files deleted.")

    print("Data downloaded and extracted successfully.")


def clean_up(folder_path):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Folder {folder_path} and its contents have been deleted.")
    except Exception as e:
        print(f"Error during cleanup: {e}")


def process_and_store_files(tmp_dir, final_dir):
    try:
        os.makedirs(final_dir, exist_ok=True)
        for root, _, files in os.walk(tmp_dir):
            for file in files:
                if file.lower().endswith((".jpg")):
                    file_path = os.path.join(root, file)
                    label = os.path.basename(os.path.dirname(
                        file_path))
                    unique_id = uuid.uuid4()

                    final_file_path = os.path.join(
                        final_dir, f"{unique_id}.jpg")
                    os.rename(file_path, final_file_path)

                    # Store metadata in the database
                    insert_image_metadata(
                        image_id=unique_id,
                        label=label,
                        dataset_name=DATASET_NAME,
                        is_training=1
                    )

    except Exception as e:
        print(f"Error during file processing: {e}")
        raise


def preprocess_images_and_labels(dataset, num_classes):

    normalization_layer = tf.keras.layers.Rescaling(1./255)
    dataset = dataset.map(lambda x, y: (
        normalization_layer(x),
        tf.one_hot(y, num_classes))).prefetch(buffer_size=tf.data.AUTOTUNE)

    images, labels = [], []
    for img, label in dataset:
        images.append(img.numpy())
        labels.append(label.numpy())

    images = np.concatenate(images, axis=0)
    labels = np.concatenate(labels, axis=0)

    return images, labels


def load_dataset(dataset_name, is_training=1, img_height=28, img_width=28):

    data_path = os.path.join(DATASET_PATH, dataset_name)
    if not os.path.exists(data_path):
        raise ValueError(f"Invalid directory: {data_path}")

    query = "SELECT id, label FROM input_data WHERE is_training = %s;"
    try:
        conn, cursor = create_connection()
        cursor.execute(query, (is_training,))
        rows = cursor.fetchall()
        if not rows:
            raise ValueError("No data found for the specified flag.")

        images, labels = [], []
        for image_id, label in rows:

            img_path = os.path.join(data_path, f"{image_id}.jpg")

            if not os.path.exists(img_path):
                print(f"Image not found for ID {image_id}, skipping.")
                continue

            img = tf.keras.utils.load_img(
                img_path, target_size=(img_height, img_width))
            images.append(tf.keras.utils.img_to_array(img) / 255.0)
            labels.append(label)

        # Encode labels
        label_names = sorted(set(labels))
        labels = np.array([label_names.index(label) for label in labels])

        images = np.array(images, dtype=np.float32)
        labels = tf.keras.utils.to_categorical(labels, len(label_names))

        return images, labels
    except Exception as e:
        raise RuntimeError(f"Error loading dataset: {e}")
    finally:
        conn.close()
