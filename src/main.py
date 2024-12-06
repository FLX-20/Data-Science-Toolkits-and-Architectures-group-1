from cnn_operations import download_data, train_model_func, test_model_func, classify_image_func
from app_config import DATASET_PATH
import argparse


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

    if args.mode == "download_data":
        download_data(args)
    elif args.mode == "train":
        train_model_func(args)
    elif args.mode == "test":
        test_model_func(args)
    elif args.mode == "classify":
        classify_image_func(args)
    elif args.mode == "all":
        download_data(args)
        train_model_func(args)
        test_model_func(args)
        classify_image_func(args)


if __name__ == "__main__":
    main()
