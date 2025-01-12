import tensorflow as tf
import numpy as np


def load_model():
    try:
        return tf.keras.models.load_model('models/mnist_cnn.keras')
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")


def model_predict(model, image_array):
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)
    return int(np.argmax(predictions))
