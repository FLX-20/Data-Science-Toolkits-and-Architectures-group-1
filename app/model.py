import tensorflow as tf
import numpy as np


def load_model():
    return tf.keras.models.load_model('models/mnist_cnn_model.keras')


def model_predict(model, image_array):
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)
    return np.argmax(predictions)
