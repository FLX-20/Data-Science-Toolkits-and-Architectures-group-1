#!/bin/bash

mkdir -p datasets models images
echo "Downloading animal image classification dataset..."
curl -L -o ./datasets/animals.zip https://www.kaggle.com/api/v1/datasets/download/borhanitrash/animal-image-classification-dataset
unzip ./datasets/animals.zip -d ./datasets
rm datasets/animals.zip

echo "Downloading flower_photos dataset..."
curl -L -o ./datasets/flower_photos.tgz https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz
tar -xzf ./datasets/flower_photos.tgz -C ./datasets
rm ./datasets/flower_photos.tgz
