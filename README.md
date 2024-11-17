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

## Pull the Docker Image from Dockerhub
Pull the image from the docker hub repo to use the CNN.
```shell
docker pull felix20/data-science-toolkits-and-architectures-group-1:cnn_image
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
    -v ./models:/app/models cnn_image \
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
    -v ./models:/app/models cnn_image \
    --mode test \
    --dataset_path /app/datasets/Animals \
    --model_file_path /app/models/cnn_model.keras \
```

## Reports
The reports of the milestones are in the `report` folder. They include further explanations about the individual milestones. 