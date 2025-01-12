from cnn_operations import download_data, test_model_func, train_model_wandb
from db_operations import overview_image, create_table, create_predictions_table


def main():

    # Create the database tables if they don't exist yet
    create_table()
    create_predictions_table()

    # Save the images to the dataset folder and store the metadata in the database
    download_data()

    # Draw an overview image of the dataset
    overview_image()

    # Train the model and log the results to Weights & Biases
    train_model_wandb()

    # Test the model on the test dataset
    test_model_func()


if __name__ == "__main__":
    main()
