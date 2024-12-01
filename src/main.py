import argparse
import os
import numpy as np
from data_loader import load_dataset, download_and_extract_zip, show_loaded_images
from models import build_cnn
from train import train_model
from evaluate import evaluate_model, predict_image_label
from save_load_models import load_model_from_keras, save_model
from db_operations import create_table
from app_config import DATASET_PATH

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

        download_and_extract_zip(
            args.url_training_data, args.dataset_name)

        print(f"Data downloaded and extracted Data")

    def train_model_func():

        print("Starting training process...")

        if not args.dataset_name:
            raise ValueError("Dataset name is required for training mode.")
        if not args.model_name:
            raise ValueError(
                "Model file path for saving the model is required.")

        (x_train, y_train), _ = load_dataset(args.dataset_name)

        num_classes = len(np.unique(y_train)) + 1
        input_shape = x_train.shape[1:]

        model = build_cnn(input_shape=input_shape, num_classes=num_classes)

        train_model(model, x_train, y_train, args.batch_size, args.epochs)

        save_model(model, args.model_name)
        print(f"Model saved successfully")

    def test_model_func():

        print("Starting testing process...")

        if not args.dataset_name:
            raise ValueError("Dataset name is required for testing mode.")
        if not args.model_name:
            raise ValueError(
                "Model file path for loading the model is required.")

        model = load_model_from_keras(args.model_name)

        _, (x_test, y_test) = load_dataset(args.dataset_name)

        evaluate_model(model, x_test, y_test)

    def classify_image_func():

        if not args.single_image_path:
            raise ValueError(
                "Single image path is required for classify mode.")
        if not args.model_name:
            raise ValueError(
                "Model file path for loading the model is required.")

        model = load_model_from_keras(args.model_name)

        predict_image_label(model, args.single_image_path)

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
        if args.single_image_path:
            classify_image_func()


if __name__ == "__main__":
    main()
