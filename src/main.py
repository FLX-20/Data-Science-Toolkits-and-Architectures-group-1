import argparse
from data_loader import load_dataset, show_loaded_images
from models import build_cnn
from train import train_model
from evaluate import evaluate_model
from model_saver import save_model
from model_loader import load_model_from_keras


def main():

    parser = argparse.ArgumentParser(
        description="Train or test the CNN model.")
    parser.add_argument("--mode", choices=["train", "test"], required=True,
                        help="Mode to run: train or test.")
    parser.add_argument("--dataset_path", type=str,
                        help="Path to the datafolder")
    parser.add_argument("--model_file_path", type=str,
                        help="Path to save the model after training and load it before testing.")
    parser.add_argument("--batch_size", type=int, default=128,
                        help="Batch size for training.")
    parser.add_argument("--epochs", type=int, default=15,
                        help="Number of epochs for training.")

    args = parser.parse_args()

    if args.mode == "train":

        if not args.dataset_path or not args.model_file_path:
            parser.error(
                "Training mode requires --dataset_path, and --model_file_path")

        (x_train, y_train), (x_test, y_test), input_shape, num_classes = load_dataset(
            args.dataset_path)

        model = build_cnn(input_shape=input_shape, num_classes=num_classes)

        train_model(model, x_train, y_train, args.batch_size, args.epochs)

        save_model(model, args.model_file_path)

    elif args.mode == "test":
        if not args.dataset_path or not args.model_file_path:
            parser.error(
                "Training mode requires --dataset_path, and --model_file_path.")

        model = load_model_from_keras(args.model_file_path)

        _, (x_test, y_test), _, _ = load_dataset(args.dataset_path)

        evaluate_model(model, x_test, y_test)


if __name__ == "__main__":
    main()
