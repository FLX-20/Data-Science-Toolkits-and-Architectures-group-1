import os
import tensorflow as tf
import wandb
from app_config import MODEL_SAVE_PATH


def load_model_from_keras(model_name):

    load_model_path = os.path.join(MODEL_SAVE_PATH, model_name + ".keras")

    try:
        model = tf.keras.models.load_model(load_model_path)
        print(f"Model loaded successfully from {load_model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def save_model(model, model_name):
    os.makedirs(MODEL_SAVE_PATH, exist_ok=True)

    model_file_path = os.path.join(MODEL_SAVE_PATH, model_name + ".keras")

    model.save(model_file_path)
    wandb.save(model_file_path)
    print(f"Model saved successfully at {model_file_path}")
