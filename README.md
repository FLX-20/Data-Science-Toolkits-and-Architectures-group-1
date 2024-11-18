# Data-Science-Toolkits-and-Architectures-group-1-

## Project Overview
This repository contains the code and resources for the subject "Data Science Toolkits and Architectures" at the University of Lucerne.

## Prerequisites
- Git 2.43.0
- Docker 27.3.1

## Download the code from the repo
A local copy of the repository can be created with the following command. Make sure that you have installed [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) before.
```shell
git clone https://github.com/FLX-20/Data-Science-Toolkits-and-Architectures-group-1.git
```

## Containerize the Application
Build the Docker image with the following command to containerize the program code.
Then you can run the commands of the next parts independent of your OS. 
```shell
docker_build -t simple_cnn
```

## Download the datasets
If this shell script is run, it creates three directories.
In the `datasets` directory, the datasets for the CNN are stored.
In the `model` directory, the trained and stored models are saved.
In the `images` directory, images are stored and created during data loading and evaluation.
Afterwards, the two datasets were downloaded and used to test the code. These datasets are `Animals` (cats, dogs, snakes) and `flower_photos` (daisy, dandelion, roses, sunflowers, tulips). 
```shell
sh scripts/download_datasets.sh
```

## Train the CNN
The model can be executed for training in a docker container by using this code. If a different dataset should be used for training change the `--dataset_path` flag. Batch size and epochs can be adapted in the same way. 
```shell
docker run --rm \
    -v ./images:/app/images \
    -v ./datasets:/app/datasets \
    -v ./models:/app/models simple_cnn \
    --mode train \
    --dataset_path /app/datasets/Animals \
    --model_file_path /app/models/cnn_model.keras \
    --batch_size 64 \
    --epochs 20
```

## Test the CNN
After training a model, it can be evaluated by executing the following command. Make sure that the file behind `--model_file_path` really exists.
```shell
docker run --rm \
    -v ./images:/app/images \
    -v ./datasets:/app/datasets \
    -v ./models:/app/models simple_cnn \
    --mode test \
    --dataset_path /app/datasets/Animals \
    --model_file_path /app/models/cnn_model.keras \
```

## Classify single Image with trained CNN
Moreover there is an option to classify single images with the trained CNN by providing the path.
Place the image in the dataset directory, so that the Docker container can access it and define the relative path of the image in the CLI, when executing the container. 
```shell
docker run --rm \
    -v ./images:/app/images \
    -v ./datasets:/app/datasets \
    -v ./models:/app/models simple_cnn \
    --mode classify \
    --single_image_path datasets/Animals/dogs/your_image_name.jpg
```

## Reports
The reports of the milestones are in the `report` folder. They include further explanations about the individual milestones. 