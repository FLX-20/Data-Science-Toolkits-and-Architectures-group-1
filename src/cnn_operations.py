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


def preprocess_image(img_path, label, img_height=28, img_width=28):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_jpeg(img, channels=3)
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

    train_dataset = create_tf_dataset(
        training_uuids, os.path.join(DATASET_PATH, DATASET_NAME), label_map)
    test_dataset = create_tf_dataset(
        testing_uuids, os.path.join(DATASET_PATH, DATASET_NAME), label_map)

    wandb_taining(train_dataset, test_dataset, label_map)


def fetch_label_map(uuids):
    placeholders = ','.join(['%s'] * len(uuids))
    query = f"SELECT id, label FROM input_data WHERE id IN ({placeholders});"
    try:
        conn, cursor = create_connection()
        cursor.execute(query, tuple(uuids))
        rows = cursor.fetchall()
    except Exception as e:
        raise RuntimeError(f"Error fetching image labels: {e}")
    finally:
        conn.close()

    label_map = {row[0]: int(row[1]) for row in rows}
    return label_map


def wandb_taining(train_dataset, test_dataset, label_map):
    # Load architectures from JSON file
    with open("architecutres/architectures.json", "r") as file:
        architectures = json.load(file)

    for arch in architectures:
        print(f"Training model: {arch['name']}")
        print(arch)

        # Initialize a new WandB run
        wandb.init(project="cnn-training", name=arch['name'], config=arch)
        config = wandb.config

        # Build the model
        model = build_model_wandb(
            config=config,
            input_shape=(config.img_height, config.img_width, 3),
            num_classes=len(set(label_map.values()))
        )

        # Define the optimizer
        optimizer = (
            tf.keras.optimizers.Adam(learning_rate=config.learning_rate)
            if config.optimizer == "adam"
            else tf.keras.optimizers.SGD(learning_rate=config.learning_rate)
        )

        # Compile the model
        model.compile(optimizer=optimizer,
                      loss="sparse_categorical_crossentropy",
                      metrics=['accuracy'])

        # Train the model
        history = model.fit(
            train_dataset,
            validation_data=test_dataset,
            epochs=config.epochs,
            callbacks=[WandbMetricsLogger()]
        )

        # Evaluate the model
        loss, accuracy = model.evaluate(test_dataset)
        print(f"Model: {arch['name']} - Loss: {loss}, Accuracy: {accuracy}")

        # Save the model
        model_dir = os.path.join(MODEL_SAVE_PATH, arch['name'])
        os.makedirs(model_dir, exist_ok=True)
        model_path = os.path.join(model_dir, f"{arch['name']}_model.keras")
        model.save(model_path)
        wandb.save(model_path)
        wandb.finish()
