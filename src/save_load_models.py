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
    model.save(model_file_path)
    print(f"Model saved in SavedModel format at {model_file_path}")
