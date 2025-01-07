import os
import numpy as np
from tensorflow import keras
from PIL import Image
import uuid
from db_operations import insert_image_metadata
from app_config import DATASET_PATH, DATASET_NAME

# Constants
DATASET_PATH = "./dataset"
TMP_FOLDER = os.path.join(DATASET_PATH, "tmp")


def create_table():
    # Placeholder for any required database or directory setup
    print("Table created or verified (placeholder function).")


def process_and_store_files():
    try:
        os.makedirs(DATASET_PATH, exist_ok=True)
        for root, _, files in os.walk(TMP_FOLDER):
            for file in files:
                if file.lower().endswith((".jpg")):
                    file_path = os.path.join(root, file)
                    label = os.path.basename(os.path.dirname(
                        file_path))
                    unique_id = uuid.uuid4()

                    final_file_path = os.path.join(
                        DATASET_PATH, f"{unique_id}.jpg")
                    os.rename(file_path, final_file_path)

                    # Store metadata in the database
                    # insert_image_metadata(
                    #     image_id=unique_id,
                    #     label=label,
                    #     dataset_name=DATASET_NAME
                    # )

    except Exception as e:
        print(f"Error during file processing: {e}")
        raise


def download_data():
    create_table()
    os.makedirs(TMP_FOLDER, exist_ok=True)

    # Load MNIST dataset
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Combine train and test data for simplicity
    x_data = np.concatenate((x_train, x_test), axis=0)
    y_data = np.concatenate((y_train, y_test), axis=0)

    # Save images in TMP_FOLDER
    for idx, (image, label) in enumerate(zip(x_data, y_data)):
        label_folder = os.path.join(TMP_FOLDER, str(label))
        os.makedirs(label_folder, exist_ok=True)

        # Save image as PNG
        image_path = os.path.join(label_folder, f"{idx}.jpg")
        img = Image.fromarray(image)
        img.save(image_path)

    print(f"Data successfully downloaded and saved in '{TMP_FOLDER}'.")

    process_and_store_files()


# Call the function
download_data()
