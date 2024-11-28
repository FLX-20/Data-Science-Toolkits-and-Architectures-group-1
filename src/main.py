import argparse
import numpy as np
from data_loader import load_dataset, download_and_extract_zip
from models import build_cnn
from train import train_model
from evaluate import evaluate_model, predict_image_label
from save_load_models import load_model_from_keras, save_model

# dev of milestone 3


def main():

    parser = argparse.ArgumentParser(
        description="Train or test the CNN model.")
    parser.add_argument("--mode", choices=["download_data", "train", "test", "classify"], required=True,
                        help="Mode to run: download training data, train or test, classify")
    parser.add_argument("--url_training_data", type=str,
                        help="url from which the training data should be downloaded")
    parser.add_argument("--model_file_path", type=str,
                        help="Path to save the model after training and load it before testing.")
    parser.add_argument("--dataset_path", type=str,
                        help="Path to the datafolder")
    parser.add_argument("--single_image_path", type=str,
                        help="Path to a single image for classification (required for classify mode).")
    parser.add_argument("--batch_size", type=int, default=128,
                        help="Batch size for training.")
    parser.add_argument("--epochs", type=int, default=15,
                        help="Number of epochs for training.")

    args = parser.parse_args()

    if args.mode == "train":

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

    elif args.mode == "test":

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

        download_and_extract_zip(args.url_training_data, './datasets')


if __name__ == "__main__":
    main()
