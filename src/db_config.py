from dotenv import load_dotenv
import os

load_dotenv()

DB_SETTINGS = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

CNN_SETTINGS = {
    "dataset_path": "datasets",
    "model_save_path": "models",
    "image_save_path": "images",
    "dataset_name": "MNIST",
    "model_name": "mnist_cnn"
}
