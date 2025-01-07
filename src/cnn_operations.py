from db_operations import create_table, create_predictions_table, create_connection, get_uuids, load_images_and_labels_by_uuids, get_metadata_by_uuids
from save_load_models import load_model_from_keras, save_model
from evaluate import evaluate_model
from train import train_model
from models import build_cnn
from db_operations import split_data_into_training_and_testing
from data_loader import process_and_store_files, clean_up
from app_config import DATASET_PATH, DATASET_NAME, BATCHE_SIZE, EPOCHS, MODEL_NAME, MODEL_SAVE_PATH
from datetime import datetime
import os
import numpy as np
import uuid
import json
import keras
import tensorflow as tf
import wandb
from PIL import Image
from wandb.integration.keras import WandbMetricsLogger
from models import build_model_wandb


def download_data():
    create_table()
    tmp_dir = os.path.join(DATASET_PATH, "tmp")
    final_dir = os.path.join(DATASET_PATH, DATASET_NAME)

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


def train_model_func():

    training_uuids = get_uuids(is_training=True)
    images, labels = load_images_and_labels_by_uuids(
        training_uuids, os.path.join(DATASET_PATH, DATASET_NAME))

    num_classes = labels.shape[1]
    input_shape = images.shape[1:]

    model = build_cnn(input_shape=input_shape, num_classes=num_classes)
    train_model(model, images, labels, BATCHE_SIZE, EPOCHS)

    save_model(model, MODEL_NAME)
    print("Model saved successfully.")


def test_model_func():

    testing_uuids = get_uuids(is_training=False)
    model = load_model_from_keras(MODEL_NAME)
    # check if model is loaded
    if not model:
        raise ValueError("Failed to load the model.")
    images, labels = load_images_and_labels_by_uuids(
        testing_uuids, os.path.join(DATASET_PATH, DATASET_NAME))

    evaluate_model(model, images, labels)


def classify_image_func():

    create_predictions_table()
    model = load_model_from_keras(MODEL_NAME)
    if not model:
        raise ValueError("Failed to load the model.")

    testing_uuids = get_uuids(is_training=True)
    images, _ = load_images_and_labels_by_uuids(
        testing_uuids, os.path.join(DATASET_PATH, DATASET_NAME))

    predictions = model.predict(images)
    predicted_indices = np.argmax(predictions, axis=1)

    label_names = sorted({row[2]
                         for row in get_metadata_by_uuids(testing_uuids)})
    predicted_labels = [label_names[idx] for idx in predicted_indices]

    try:
        conn, cursor = create_connection()
        for image_id, predicted_label in zip(testing_uuids, predicted_labels):
            prediction_id = str(uuid.uuid4())
            prediction_timestamp = datetime.now()

            query = """
            INSERT INTO predictions (id, image_id, predicted_label, model_name, prediction_timestamp)
            VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(
                query, (prediction_id, str(image_id), predicted_label,
                        MODEL_NAME, prediction_timestamp)
            )
        conn.commit()
        print("Predictions stored successfully in the database.")
    except Exception as e:
        print(f"Error storing predictions: {e}")
    finally:
        conn.close()


def train_model_wandb():

    training_uuids = get_uuids(is_training=True)
    testing_uuids = get_uuids(is_training=False)

    images, labels = load_images_and_labels_by_uuids(
        training_uuids, os.path.join(DATASET_PATH, DATASET_NAME))
    test_images, test_labels = load_images_and_labels_by_uuids(
        testing_uuids, os.path.join(DATASET_PATH, DATASET_NAME))

    wandb_taining(images, labels, test_images, test_labels)


def wandb_taining(x_train, y_train, x_test, y_test):

    with open("architecutres/architectures.json", "r") as file:
        architectures = json.load(file)

    for arch in architectures:
        print(f"Training model: {arch['name']}")
        print(arch)

        wandb.init(project="cnn-training", name=arch['name'], config=arch)
        config = wandb.config
        print(config)

        model = build_model_wandb(
            config, input_shape=x_train.shape, num_classes=y_train.shape[1])

        optimizer = tf.keras.optimizers.Adam(learning_rate=config.learning_rate) \
            if config.optimizer == "adam" else tf.keras.optimizers.SGD(learning_rate=config.learning_rate)
        model.compile(optimizer=optimizer,
                      loss="categorical_crossentropy", metrics=['accuracy'])

        history = model.fit(
            x_train, y_train,
            epochs=config.epochs,
            batch_size=config.batch_size,
            validation_data=(x_test, y_test),
            callbacks=[WandbMetricsLogger()]
        )

        loss, accuracy = model.evaluate(x_test, y_test)
        print(f"Model: {arch['name']} - Loss: {loss}, Accuracy: {accuracy}")

        directory = os.path.dirname(
            f"{MODEL_SAVE_PATH}/{arch['name']}_model.keras")

        if not os.path.exists(directory):
            os.makedirs(directory)

        model_path = f"{MODEL_SAVE_PATH}/{arch['name']}_model.keras"
        model.save(model_path)
        wandb.save(model_path)
        wandb.finish()
