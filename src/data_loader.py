from db_operations import insert_image_metadata
import uuid
import pathlib
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import zipfile
import urllib.request
import os


def download_and_extract_zip(url, datasets_dir, dataset_name):
    try:
        # Create necessary directories
        tmp_dir = os.path.join(datasets_dir, "tmp")
        final_dir = os.path.join(datasets_dir, dataset_name)
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
                    print(f"Image {file} processed and moved to {
                          final_file_path}")

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
    data_path,
    batch_size=32,
    img_height=180,
    img_width=180,
    validation_split=0.2,
    seed=10
):
    data_dir = pathlib.Path(data_path)

    if not (data_dir.exists() and data_dir.is_dir()):
        return f"'{data_path}' is not a valid directory."

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_path,
        validation_split=validation_split,
        subset="training",
        seed=seed,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_path,
        validation_split=validation_split,
        subset="validation",
        seed=seed,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    class_names = train_ds.class_names
    num_classes = len(class_names)

    show_loaded_images(train_ds, class_names, 9,
                       "images/examples_train_images")
    show_loaded_images(val_ds, class_names, 9,
                       "images/examples_test_images")

    x_train, y_train = preprocess_images_and_labels(train_ds, num_classes)
    x_test, y_test = preprocess_images_and_labels(val_ds, num_classes)

    return (x_train, y_train), (x_test, y_test)


def show_loaded_images(dataset, class_names, num_images=0, filename="images.png"):
    plt.figure(figsize=(10, 10))
    for images, labels in dataset.take(1):
        for i in range(min(num_images, len(images))):
            ax = plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")
    plt.savefig(filename)
    print(f"Overview of images and their classes are stored in {filename}")
