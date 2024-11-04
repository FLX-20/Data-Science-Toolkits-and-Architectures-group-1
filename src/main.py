import numpy as np
import keras
from keras import layers
from data_loader import load_preprocess_data
from models import build_mnist_cnn
from train import train_model
from config import batch_size, epochs

# Load and preprocess data
(x_train, y_train), (x_test, y_test) = load_preprocess_data()

# Define model
model = build_mnist_cnn()

# Train model
train_model(model, x_train, y_train)


"""
## Evaluate the trained model
"""

score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])