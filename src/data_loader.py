import pathlib
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


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
