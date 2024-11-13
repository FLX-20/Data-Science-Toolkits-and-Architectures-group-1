import argparse
import config
from data_loader import load_dataset
from models import build_mnist_cnn
from train import train_model
from evaluate import evaluate_model
from model_saver import save_model
from model_loader import load_model_from_keras


def main():

    parser = argparse.ArgumentParser(description="Train or test the CNN model.")
    parser.add_argument("--mode", choices=["train", "test"], required=True, help="Mode to run: train or test.")
    parser.add_argument("--dataset_path", type=str, help="Path to the .tgz dataset file for training.")
    parser.add_argument("--extract_to", type=str, help="Path to extract the dataset.")
    parser.add_argument("--save_model_path", type=str, help="Path to save the trained model.")
    parser.add_argument("--load_model_path", type=str, help="Path to load the model for testing.")

    args = parser.parse_args()

    if args.mode == "train":

        if not args.dataset_path or not args.extract_to or not args.save_model_path:
            parser.error("Training mode requires --dataset_path, --extract_to, and --save_model_path.")

        config.save_path = args.save_model_path

        # Load and preprocess data ("datasets/flower_photos.tgz", "datasets")
        (x_train, y_train), (x_test, y_test) = load_dataset(args.dataset_path, args.extract_to)

        # Define model with dynamic input shape and class count
        model = build_mnist_cnn()

        # Train model
        train_model(model, x_train, y_train)

        # Save trained model
        save_model(model)

    # Testing mode
    elif args.mode == "test":
        if not args.load_model_path:
            parser.error("Testing mode requires --load_model_path.")

        # Load model
        model = load_model_from_keras(args.load_model_path)
        print(model)

        # Load test data (assuming extraction already done)
        _, (x_test, y_test) = load_dataset(args.dataset_path, args.extract_to)

        # Evaluate model
        evaluate_model(model, x_test, y_test)

if __name__ == "__main__":
    main()
