import uuid
import shutil
import random
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from app_config import DATASET_PATH, IMAGE_SAVE_PATH, DATASET_NAME
from db_operations import insert_image_metadata, create_connection


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
                        dataset_name=DATASET_NAME
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


def load_dataset(dataset_name, is_training=True, img_height=180, img_width=180):
    """
    Loads dataset based on training/testing flag.
    """
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


def show_loaded_images(images, labels, class_names, num_images=9, filename="examples_images.jpg"):

    os.makedirs(IMAGE_SAVE_PATH, exist_ok=True)
    file_path = os.path.join(IMAGE_SAVE_PATH, filename)

    if len(images) < num_images:
        num_images = len(images)

    random_indices = random.sample(range(len(images)), num_images)

    plt.figure(figsize=(10, 10))
    for i, idx in enumerate(random_indices):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[idx])
        plt.title(class_names[np.argmax(labels[idx])])
        plt.axis("off")
    plt.savefig(file_path)
    print(f"Overview of input_data and their classes are stored in {
          file_path}")
