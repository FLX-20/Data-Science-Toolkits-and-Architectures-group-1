FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --default-timeout=100000 tensorflow==2.18.0
RUN pip install --no-cache-dir --default-timeout=100000 -r requirements.txt

# Expose the application port
EXPOSE 8000

# Run the application
#CMD ["python", "src/main.py", "--mode", "train","--model_file_path","model/cnn_model.keras","--dataset_path","datasets/Animals"]
#CMD ["python", "src/main.py", "--mode", "download_data","--url_training_data","https://www.kaggle.com/api/v1/datasets/download/borhanitrash/animal-image-classification-dataset","--dataset_name","Animals"]
CMD ["python", "src/main.py", "--mode", "all", "--url_training_data", "https://www.kaggle.com/api/v1/datasets/download/borhanitrash/animal-image-classification-dataset", "--dataset_name", "Animals", "--model_name", "cnn_model", "--batch_size", "8", "--epochs", "15"]
