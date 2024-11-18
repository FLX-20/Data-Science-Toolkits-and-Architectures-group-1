#!/bin/bash

echo "================================================================================================================
               Welcome to the Docker Container!$                     
================================================================================================================

This container is for running and training our Convolutional Neural Network.
Two datasets are already downloaded in the data set folder to train and test the model.

1. Train the model using the Animals dataset:
   Command: src/main.py --mode train --model_file_path models/animals.keras --dataset_path datasets/Animals

2. Test the model using the Animals dataset:
   Command: src/main.py --mode test --model_file_path models/animals.keras --dataset_path datasets/Animals

3. Train the model using the Flower Photos dataset:
   Command: src/main.py --mode train --model_file_path models/animals.keras --dataset_path datasets/flower_photos

4. Test the model using the Flower Photos dataset:
   Command: src/main.py --mode test --model_file_path models/animals.keras --dataset_path datasets/flower_photos

================================================================================================================
"

# Keep the container running or start a shell
exec "$@"