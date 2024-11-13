from data_loader import load_dataset
from models import build_mnist_cnn
from train import train_model
from evaluate import evaluate_model
from model_saver import save_model

# Load and preprocess data
(x_train, y_train), (x_test, y_test), input_shape, num_classes = load_dataset("datasets/flower_photos.tgz", "datasets")

# Define model with dynamic input shape and class count
model = build_mnist_cnn(input_shape, num_classes)

# Train model
train_model(model, x_train, y_train)

# Save trained model
save_model(model)

# Evaluate model
evaluate_model(model, x_test, y_test)
