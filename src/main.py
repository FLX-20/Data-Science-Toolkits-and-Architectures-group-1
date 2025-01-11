from cnn_operations import download_data, test_model_func, train_model_wandb
from db_operations import overview_image


def main():

    download_data()
    overview_image()
    train_model_wandb()
    test_model_func()


if __name__ == "__main__":
    main()
