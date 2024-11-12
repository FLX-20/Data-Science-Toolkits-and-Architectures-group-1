from data_loader import load_preprocess_data, download_data_from_url
from models import build_mnist_cnn
from train import train_model
from evaluate import evaluate_model


data_dir = download_data_from_url("https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz")

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

# Load and preprocess data
(x_train, y_train), (x_test, y_test) = load_preprocess_data()

# Define model
model = build_mnist_cnn()

# Train model
train_model(model, x_train, y_train)

# Evaluate model
evaluate_model(model, x_test, y_test)
