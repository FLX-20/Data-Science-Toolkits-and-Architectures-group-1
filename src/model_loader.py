import tensorflow as tf

def load_model_from_keras(load_model_path = None):
    try:
        model = tf.keras.models.load_model(load_model_path)
        print(f"Model loaded successfully from {load_model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None