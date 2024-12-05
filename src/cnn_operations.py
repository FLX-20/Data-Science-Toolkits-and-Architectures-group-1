from db_operations import create_table, create_predictions_table, create_connection, get_uuids, load_images_and_labels_by_uuids, get_metadata_by_uuids
from save_load_models import load_model_from_keras, save_model
from evaluate import evaluate_model
from train import train_model
from models import build_cnn
from data_loader import download_and_prepare_dataset
from app_config import DATASET_PATH
from datetime import datetime
import os
import numpy as np
import uuid


def download_data(args):
    if not args.url_training_data or not args.dataset_name:
        raise ValueError(
            "URL and dataset name are required for downloading data.")

    create_table()
    os.makedirs(DATASET_PATH, exist_ok=True)
    download_and_prepare_dataset(args.url_training_data, args.dataset_name)
    print("Data downloaded and extracted successfully.")


def train_model_func(args):
    print("Starting training process...")
    if not args.dataset_name:
        raise ValueError("Dataset name is required for training mode.")
    if not args.model_name:
        raise ValueError("Model file path for saving the model is required.")

    training_uuids = get_uuids(is_training=True)
    images, labels = load_images_and_labels_by_uuids(
        training_uuids, os.path.join(DATASET_PATH, args.dataset_name))

    num_classes = labels.shape[1]
    input_shape = images.shape[1:]

    model = build_cnn(input_shape=input_shape, num_classes=num_classes)
    train_model(model, images, labels, args.batch_size, args.epochs)

    save_model(model, args.model_name)
    print("Model saved successfully.")


def test_model_func(args):
    print("Starting testing process...")
    if not args.dataset_name:
        raise ValueError("Dataset name is required for testing mode.")
    if not args.model_name:
        raise ValueError("Model file path for loading the model is required.")

    testing_uuids = get_uuids(is_training=False)
    model = load_model_from_keras(args.model_name)
    images, labels = load_images_and_labels_by_uuids(
        testing_uuids, os.path.join(DATASET_PATH, args.dataset_name))

    evaluate_model(model, images, labels)


def classify_image_func(args):
    create_predictions_table()
    model = load_model_from_keras(args.model_name)
    if not model:
        raise ValueError("Failed to load the model.")

    testing_uuids = get_uuids(is_training=True)
    images, _ = load_images_and_labels_by_uuids(
        testing_uuids, os.path.join(DATASET_PATH, args.dataset_name))

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
            INSERT INTO image_predictions (id, image_id, predicted_label, model_name, prediction_timestamp)
            VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(
                query, (prediction_id, str(image_id), predicted_label,
                        args.model_name, prediction_timestamp)
            )
        conn.commit()
        print("Predictions stored successfully in the database.")
    except Exception as e:
        print(f"Error storing predictions: {e}")
    finally:
        conn.close()
