from cnn_operations import test_model, train_model_wandb
from db_operations import create_table, create_predictions_table, overview_image
from data_loader import download_data


def main():

    # Create tables if not exist yet
    create_table()
    create_predictions_table()

    # # Download , process and store data and metadata in the database
    download_data()

    # # Save class overview image
    overview_image()

    # # Train the model with Weights and Biases
    train_model_wandb()

    # Test the model
    test_model()


if __name__ == "__main__":
    main()
