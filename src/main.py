from cnn_operations import download_data, train_model_func, test_model_func, classify_image_func, train_model_wandb
from app_config import DATASET_PATH
import argparse

# dev for milestone 4


def main():
    parser = argparse.ArgumentParser(
        description="Train or test the CNN model.")
    parser.add_argument("--mode", choices=["download_data", "train", "test", "classify", "all", "wandb_run"], required=True,
                        help="Mode to run: download training data, train or test, classify, or run all steps")

    args = parser.parse_args()

    if args.mode == "download_data":
        download_data()
    elif args.mode == "train":
        train_model_func()
    elif args.mode == "test":
        test_model_func()
    elif args.mode == "wandb_run":
        # download_data()
        # train_model_wandb()
        test_model_func()
    elif args.mode == "all":
        download_data()
        train_model_func()
        test_model_func()
        classify_image_func()


if __name__ == "__main__":
    main()
