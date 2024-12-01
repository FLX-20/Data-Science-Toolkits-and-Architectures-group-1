from db_operations import get_image_metadata_by_uuid
from db_operations import insert_image_metadata
import uuid
import random
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import zipfile
import urllib.request
import os
from app_config import DATASET_PATH, IMAGE_SAVE_PATH


def download_and_extract_zip(url, dataset_name):
    try:
        # Create necessary directories
        tmp_dir = os.path.join(DATASET_PATH, "tmp")
        final_dir = os.path.join(DATASET_PATH, dataset_name)
        os.makedirs(tmp_dir, exist_ok=True)
        os.makedirs(final_dir, exist_ok=True)

        # Download the ZIP file
        filename = url.split('/')[-1]
        print(f"Downloading {url}...")
        local_zip_path = os.path.join(tmp_dir, filename)
        urllib.request.urlretrieve(url, local_zip_path)
        print(f"Downloaded to {local_zip_path}")

        # Extract ZIP file to temporary folder
        print(f"Extracting contents to {tmp_dir}...")
        with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
            zip_ref.extractall(tmp_dir)
        print("Extraction complete.")

        # Process extracted files and move them to the final folder
        for root, _, files in os.walk(tmp_dir):
            for file in files:
                if file.lower().endswith((".png", ".jpg", ".jpeg")):
                    file_path = os.path.join(root, file)
                    label = os.path.basename(os.path.dirname(
                        file_path))  # Folder name as label
                    unique_id = uuid.uuid4()

                    # Move file to the final dataset folder
                    final_file_path = os.path.join(
                        final_dir, f"{unique_id}_{file}")
                    os.rename(file_path, final_file_path)

                    # Store metadata in the database
                    insert_image_metadata(
                        image_id=unique_id,
                        url=url,
                        file_path=final_file_path,
                        label=label,
                        dataset_name=dataset_name
                    )

        # Clean up temporary folder
        os.remove(local_zip_path)
        os.rmdir(tmp_dir)
        print(f"Temporary files deleted.")

        return final_dir
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


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


def load_dataset(
    dataset_name,
    img_height=180,
    img_width=180,
    validation_split=0.2,
    seed=10
):
    data_path = os.path.join(DATASET_PATH, dataset_name)

    if not os.path.exists(data_path):
        raise ValueError(f"'{data_path}' is not a valid directory.")

    # Load all image file paths
    image_paths = [os.path.join(data_path, f) for f in os.listdir(
        data_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_paths:
        raise ValueError(
            f"No images found in the specified directory {data_path}")

    # Retrieve metadata for labels from the database
    images, labels = [], []
    for image_path in image_paths:
        # Assuming the filename contains the UUID to match metadata
        image_uuid = os.path.basename(image_path).split("_")[0]
        metadata = get_image_metadata_by_uuid(image_uuid)
        if metadata and metadata["label"]:
            img = tf.keras.utils.load_img(
                image_path, target_size=(img_height, img_width))
            img = tf.keras.utils.img_to_array(img) / 255.0
            images.append(img)
            labels.append(metadata["label"])
        else:
            print(f"Metadata not found for image: {image_path}, skipping.")

    # Convert lists to NumPy arrays
    images = np.array(images, dtype=np.float32)
    labels = np.array(labels)

    # Encode labels into numeric format
    label_names = sorted(set(labels))
    label_to_index = {name: idx for idx, name in enumerate(label_names)}
    labels = np.array([label_to_index[label] for label in labels])

    # Shuffle and split data into training and validation sets
    indices = np.arange(len(images))
    np.random.seed(seed)
    np.random.shuffle(indices)

    split_idx = int(len(images) * (1 - validation_split))
    train_indices, val_indices = indices[:split_idx], indices[split_idx:]

    x_train, y_train = images[train_indices], labels[train_indices]
    x_val, y_val = images[val_indices], labels[val_indices]

    # One-hot encode labels
    num_classes = len(label_names)
    y_train = tf.keras.utils.to_categorical(y_train, num_classes)
    y_val = tf.keras.utils.to_categorical(y_val, num_classes)

    show_loaded_images(x_train, y_train, label_names)

    return (x_train, y_train), (x_val, y_val)


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
    print(f"Overview of images and their classes are stored in {file_path}")
