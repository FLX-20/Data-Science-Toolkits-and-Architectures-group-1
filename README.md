# Data-Science-Toolkits-and-Architectures-group-1-

## Project Overview
This repository contains the code and resources for the subject "Data Science Toolkits and Architectures" at the University of Lucerne.
The final result of this project is a multi-container Flask web application for classifying digits using PostgreSQL, Keras, TensorFlow, docker, weights and biases, docker-compose, nginx, gunicorn and git.

## Prerequisites
- Git 2.43.0
- Docker 27.3.1
- Docker Compose 1.29.1

## Executing the Code
The entire code can be executed using the following command in the CLI, provided it is executed in the root directory of the cloned repository:
```shell
docker-compose up
```
After executing this command, the Flask web application is started. This application can be accessed at the following URL: `localhost:8080`.
Additionally, you can send images to the API with a `POST` request to the application, for example using [postman](https://www.postman.com/) which returns the predicted value in JSON format.  
It is important to note that, at the same time, the CNN is retrained in the `app` container. If you do not want to retrain the model each time, comment out this part in the compose.yaml file.  
The results of the training process are transmitted to the related public [weights and bias project](https://wandb.ai/fe-pappe-dsta-1/cnn-training/workspace).  
After successfully training the network, you can find the related confusion matrix and an overview image of all classes in the created `images` directory.

Moreover, it is important to note that an .env file must be created before the code can be successfully executed. This file should include the following variables:
```
POSTGRES_USER=your_user_name
POSTGRES_PASSWORD=your_pwd
PGADMIN_DEFAULT_EMAIL=your_email
PGADMIN_DEFAULT_PASSWORD=your_pwd
DB_NAME=milestone_5
SECRET_KEY = your_secret_key
WANDB_API_KEY=your_weights_and_biases_key
```
Once all containers are running, you can open the Flask web application at `localhost:8080`.
The database can be viewed and edited with pgAdmin at `localhost:5050`.





