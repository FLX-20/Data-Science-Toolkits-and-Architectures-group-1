# Data-Science-Toolkits-and-Architectures-group-1-

## Project Overview
This repository contains the code and resources for the subject "Data Science Toolkits and Architectures" at the University of Lucerne.

## Prerequisites
- Git 2.43.0
- Docker 27.3.1
- Docker Compose 1.29.1

## Executing the Code
The entire code can be executed by the following command in the CLI, if it is executed in the root directory of the cloned repository.
```shell
docker compose up
```
After the execution of this command, three different CNNs are trained and evaluated. The results are transmitted to the related public [weights and bias project](https://wandb.ai/fe-pappe-dsta-1/cnn-training/workspace).
Moreover, it is important to notice that an `.env' file has to be created before the code can be successfully executed. This file should include the following variables.
```
POSTGRES_USER=your_user_name
POSTGRES_PASSWORD=your_pwd
PGADMIN_DEFAULT_EMAIL=your_email
PGADMIN_DEFAULT_PASSWORD=your_pwd
DB_NAME=milestone_4
WANDB_API_KEY=your_weights_and_biases_key
```

Then the program code of the application container will execute the following steps:
- Downloading the training and testing data
- Training three different CNNs (small, medium, large)
- Share the evaluation results in a weights and biases project