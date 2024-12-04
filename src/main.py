from db_operations import create_table, create_predictions_table, create_connection, get_uuids, load_images_and_labels_by_uuids
from app_config import DATASET_PATH
from save_load_models import load_model_from_keras, save_model
from evaluate import evaluate_model
from train import train_model
from models import build_cnn
from data_loader import load_dataset,  download_and_prepare_dataset
from datetime import datetime
import argparse
import os
import numpy as np
import uuid

# python src/main.py --mode train --model_name model/cnn_model.keras --dataset_path datasets/Animals
# python src/main.py --mode test --model_name model/cnn_model.keras --dataset_path datasets/Animals
# python src/main.py --mode classify --model_name model/cnn_model.keras --single_image_path image/cat.jpeg


def main():

    parser = argparse.ArgumentParser(
        description="Train or test the CNN model.")
    parser.add_argument("--mode", choices=["download_data", "train", "test", "classify", "all"], required=True,
                        help="Mode to run: download training data, train or test, classify, or run all steps")
    parser.add_argument("--url_training_data", type=str,
                        help="URL from which the training data should be downloaded")
    parser.add_argument("--dataset_name", type=str,
                        help="The name of the dataset")
    parser.add_argument("--model_name", type=str,
                        help="Give the model name")
    parser.add_argument("--dataset_path", type=str, default=DATASET_PATH,
                        help="Path to the data folder")
    parser.add_argument("--single_image_path", type=str,
                        help="Path to a single image for classification (required for classify mode).")
    parser.add_argument("--batch_size", type=int, default=128,
                        help="Batch size for training.")
    parser.add_argument("--epochs", type=int, default=15,
                        help="Number of epochs for training.")

    args = parser.parse_args()
    print("Entered arguments:", vars(args))

    def download_data():

        if not args.url_training_data or not args.dataset_name:
            raise ValueError(
                "URL and dataset name are required for downloading data.")

        create_table()

        os.makedirs(DATASET_PATH, exist_ok=True)

        download_and_prepare_dataset(
            args.url_training_data, args.dataset_name)

        print(f"Data downloaded and extracted Data")

    def train_model_func():

        print("Starting training process...")

        if not args.dataset_name:
            raise ValueError("Dataset name is required for training mode.")
        if not args.model_name:
            raise ValueError(
                "Model file path for saving the model is required.")

        # Fetch UUIDs for training
        training_uuids = get_uuids(is_training=True)

        # Load images and labels for training
        images, labels = load_images_and_labels_by_uuids(
            training_uuids, os.path.join(DATASET_PATH, args.dataset_name))

        num_classes = labels.shape[1]
        input_shape = images.shape[1:]

        model = build_cnn(input_shape=input_shape, num_classes=num_classes)

        train_model(model, images, labels, args.batch_size, args.epochs)

        save_model(model, args.model_name)
        print(f"Model saved successfully")

    def test_model_func():

        print("Starting testing process...")

        if not args.dataset_name:
            raise ValueError("Dataset name is required for testing mode.")
        if not args.model_name:
            raise ValueError(
                "Model file path for loading the model is required.")

        # Fetch UUIDs for testing
        testing_uuids = get_uuids(is_training=False)

        model = load_model_from_keras(args.model_name)

        # Load images and labels for testing
        images, labels = load_images_and_labels_by_uuids(
            testing_uuids, os.path.join(DATASET_PATH, args.dataset_name))

        evaluate_model(model, images, labels)

    def classify_image_func():
        if not args.dataset_name:
            raise ValueError("Dataset name is required for classify mode.")
        if not args.model_name:
            raise ValueError(
                "Model file path for loading the model is required.")

        # Ensure the predictions table exists
        create_predictions_table()

        # Load the model
        model = load_model_from_keras(args.model_name)

        # Load the test data
        x_test, _ = load_dataset(args.dataset_name, is_training=False)

        # Predict on the test data
        predictions = model.predict(x_test)
        predicted_labels = np.argmax(predictions, axis=1)

        # Save predictions to the database
        try:
            conn, cursor = create_connection()
            for image_idx, predicted_label in enumerate(predicted_labels):
                query = """
                INSERT INTO image_predictions (id, image_id, predicted_label, model_name, prediction_timestamp)
                VALUES (%s, %s, %s, %s, %s);
                """
                # Generate a new UUID for the prediction
                prediction_id = str(uuid.uuid4())

                # Assuming `image_id` is retrievable; adapt if x_test does not include it
                # Modify if image_id is not directly available
                image_id = x_test[image_idx]
                prediction_timestamp = datetime.now()

                cursor.execute(query, (prediction_id, image_id, str(
                    predicted_label), args.model_name, prediction_timestamp))

            conn.commit()
            print("Predictions stored successfully in the database.")
        except Exception as e:
            print(f"Error storing predictions: {e}")
        finally:
            conn.close()

    if args.mode == "download_data":
        download_data()
    elif args.mode == "train":
        train_model_func()
    elif args.mode == "test":
        test_model_func()
    elif args.mode == "classify":
        classify_image_func()
    elif args.mode == "all":
        download_data()
        train_model_func()
        test_model_func()
        # classify_image_func()


if __name__ == "__main__":
    main()
