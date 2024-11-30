import argparse
import numpy as np
from data_loader import load_dataset, download_and_extract_zip, show_loaded_images
from models import build_cnn
from train import train_model
from evaluate import evaluate_model, predict_image_label
from save_load_models import load_model_from_keras, save_model
from db_operations import create_table

# python src/main.py --mode train --model_file_path models/cnn_model.keras --dataset_path datasets/Animals

DATASET_PATH = "datasets"
MODEL_SAVE_PATH = "models/model.keras"


def main():

    parser = argparse.ArgumentParser(
        description="Train or test the CNN model.")
    parser.add_argument("--mode", choices=["download_data", "train", "test", "classify"], required=True,
                        help="Mode to run: download training data, train or test, classify")
    parser.add_argument("--url_training_data", type=str,
                        help="url from which the training data should be downloaded")
    parser.add_argument("--model_file_path", type=str, default=MODEL_SAVE_PATH,
                        help="Path to save the model after training and load it before testing.")
    parser.add_argument("--dataset_path", type=str, default=DATASET_PATH,
                        help="Path to the datafolder")
    parser.add_argument("--single_image_path", type=str,
                        help="Path to a single image for classification (required for classify mode).")
    parser.add_argument("--batch_size", type=int, default=128,
                        help="Batch size for training.")
    parser.add_argument("--epochs", type=int, default=15,
                        help="Number of epochs for training.")

    args = parser.parse_args()
    print("Entered arguments:", vars(args))

    if args.mode == "train":

        print("Starting training process...")
        if not args.dataset_path:
            raise ValueError("Dataset path is required for training mode.")
        if not args.model_file_path:
            raise ValueError(
                "model file path for saving the model is required")

        (x_train, y_train), (x_test, y_test) = load_dataset(args.dataset_path)

        num_classes = len(np.unique(y_train)) + 1
        input_shape = x_train.shape[1:]

        model = build_cnn(input_shape=input_shape, num_classes=num_classes)

        train_model(model, x_train, y_train, args.batch_size, args.epochs)

        save_model(model, args.model_file_path)
        print(f"Model saved to {args.model_file_path}")

    elif args.mode == "test":

        print("Starting testing process...")
        if not args.dataset_path:
            raise ValueError("Dataset path is required for testing mode.")
        if not args.model_file_path:
            raise ValueError(
                "model file path for loading the model is required")

        model = load_model_from_keras(args.model_file_path)

        _, (x_test, y_test) = load_dataset(args.dataset_path)

        evaluate_model(model, x_test, y_test)

    elif args.mode == "classify":

        if not args.single_image_path:
            raise ValueError(
                "Single image path is required for classify mode.")
        if not args.model_file_path:
            raise ValueError(
                "model file path for loading the model is required")

        model = load_model_from_keras(args.model_file_path)
        predict_image_label(model, args.single_image_path)

    elif args.mode == "download_data":

        if not args.url_training_data:
            raise ValueError(
                "url is reuqired to download the data")

        create_table()

        download_and_extract_zip(
            args.url_training_data, DATASET_PATH, dataset_name="Animals")
        print(f"Data downloaded and extracted to {args.dataset_path}")


if __name__ == "__main__":
    main()
