import os
import tensorflow as tf


def load_model_from_keras(load_model_path):
    try:
        model = tf.keras.models.load_model(load_model_path)
        print(f"Model loaded successfully from {load_model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def save_model(model, model_file_path):

    os.makedirs(os.path.dirname(model_file_path), exist_ok=True)

    if model_file_path.endswith(".keras") or model_file_path.endswith(".h5"):
        model.save(model_file_path)
        print(f"Model saved successfully at {model_file_path}")
    else:
        raise ValueError(
            "Invalid file extension. Please use '.keras' or '.h5' for the file path."
        )
