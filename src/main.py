import numpy as np
import keras
from keras import layers
from data_loader import load_preprocess_data
from models import build_mnist_cnn
from config import batch_size, epochs

# Load and preprocess data
(x_train, y_train), (x_test, y_test) = load_preprocess_data()

# define model
model = build_mnist_cnn()

"""
## Train the model
"""

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

"""
## Evaluate the trained model
"""

score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])