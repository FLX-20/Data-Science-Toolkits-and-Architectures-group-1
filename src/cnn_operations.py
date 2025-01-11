from db_operations import create_table, create_predictions_table, get_uuids, load_images_and_labels_by_uuids, fetch_label_map
from save_load_models import load_model_from_keras, save_model
from evaluate import evaluate_model, plot_confusion_matrix
from db_operations import split_data_into_training_and_testing
from data_loader import process_and_store_files, clean_up
from app_config import DATASET_PATH, DATASET_NAME, MODEL_NAME
import os
import numpy as np
import json
import keras
import tensorflow as tf
import wandb
from PIL import Image
from wandb.integration.keras import WandbMetricsLogger
from models import build_model_wandb


def download_data():

    final_dir = os.path.join(DATASET_PATH, DATASET_NAME)

    if os.path.exists(final_dir):
        print(f"The dataset '{
              DATASET_NAME}' already exists. Skipping download.")
        return

    create_table()
    create_predictions_table()
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

    split_data_into_training_and_testing()

    clean_up(tmp_dir)
    print("Temporary files deleted.")

    print("Data downloaded and extracted successfully.")


def test_model_func():
    testing_uuids = get_uuids(is_training=False)
    model = load_model_from_keras(MODEL_NAME)

    if not model:
        raise ValueError("Failed to load the model.")

    images, labels = load_images_and_labels_by_uuids(
        testing_uuids, os.path.join(DATASET_PATH, DATASET_NAME))

    images = tf.image.rgb_to_grayscale(images).numpy()
    images = images.reshape(images.shape[0], 28, 28, 1)

    print(f"Images shape after conversion: {images.shape}")
    print("Plotting confusion matrix")
    evaluate_model(model, images, labels)
    plot_confusion_matrix(model, images, labels)


def preprocess_image(img_path, label, img_height=28, img_width=28):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_jpeg(img, channels=1)
    img = tf.image.resize(img, [img_height, img_width])
    img = img / 255.0
    label = tf.cast(label, tf.int32)
    return img, label


def create_tf_dataset(uuids, dataset_path, label_map, batch_size=32, img_height=28, img_width=28):
    # Map UUIDs to file paths and labels
    img_paths = [os.path.join(dataset_path, f"{uuid}.jpg") for uuid in uuids]
    labels = [label_map[uuid] for uuid in uuids]

    # Create a TensorFlow dataset
    dataset = tf.data.Dataset.from_tensor_slices((img_paths, labels))
    dataset = dataset.map(lambda x, y: preprocess_image(x, y, img_height, img_width),
                          num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.shuffle(buffer_size=1000).batch(
        batch_size).prefetch(tf.data.AUTOTUNE)

    return dataset


def train_model_wandb():
    training_uuids = get_uuids(is_training=True)
    testing_uuids = get_uuids(is_training=False)

    label_map = fetch_label_map(training_uuids + testing_uuids)

    # Filter out UUIDs that were excluded
    training_uuids = [uuid for uuid in training_uuids if uuid in label_map]
    testing_uuids = [uuid for uuid in testing_uuids if uuid in label_map]

    train_dataset = create_tf_dataset(
        training_uuids, os.path.join(DATASET_PATH, DATASET_NAME), label_map)
    test_dataset = create_tf_dataset(
        testing_uuids, os.path.join(DATASET_PATH, DATASET_NAME), label_map)

    wandb_taining(train_dataset, test_dataset, label_map)


def wandb_taining(train_dataset, test_dataset, label_map):

    with open("architecutres/architectures.json", "r") as file:
        architectures = json.load(file)

    for arch in architectures:
        print(f"Training model: {arch['name']}")
        print(arch)

        wandb.init(project="cnn-training", name=arch['name'], config=arch)
        config = wandb.config

        model = build_model_wandb(
            config=config,
            input_shape=(config.img_height, config.img_width, 1),
            num_classes=len(set(label_map.values()))
        )

        optimizer = (
            tf.keras.optimizers.Adam(learning_rate=config.learning_rate)
            if config.optimizer == "adam"
            else tf.keras.optimizers.SGD(learning_rate=config.learning_rate)
        )

        model.compile(optimizer=optimizer,
                      loss="sparse_categorical_crossentropy",
                      metrics=['accuracy'])

        history = model.fit(
            train_dataset,
            validation_data=test_dataset,
            epochs=config.epochs,
            callbacks=[WandbMetricsLogger()]
        )

        loss, accuracy = model.evaluate(test_dataset)
        print(f"Model: {arch['name']} - Loss: {loss}, Accuracy: {accuracy}")

        save_model(model, arch['name'])

        # model_dir = os.path.join(MODEL_SAVE_PATH)
        # os.makedirs(model_dir, exist_ok=True)
        # model_path = os.path.join(model_dir, f"{arch['name']}.keras")
        # model.save(model_path)
        # wandb.save(model_path)
        wandb.finish()
