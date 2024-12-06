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

    if model_file_path.endswith(".keras"):
        model.save(model_file_path, save_format="keras")
        print(f"Model saved in Keras format at {model_file_path}")
    elif model_file_path.endswith(".h5"):
        model.save(model_file_path, save_format="h5")
        print(f"Model saved in HDF5 format at {model_file_path}")
    else:
        raise ValueError(
            "Invalid file extension. Please use '.keras' or '.h5' for the file path.")
