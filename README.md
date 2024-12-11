# Data-Science-Toolkits-and-Architectures-group-1-

## Project Overview
This repository contains the code and resources for the subject "Data Science Toolkits and Architectures" at the University of Lucerne.

## Prerequisites
- Git 2.43.0
- Docker 27.3.1

## Executing the Code
The entire code can be executed by the following command in the CLI, if it is executed in the root directory of the cloned repository.
```shell
docker compose up
```
This command downloads docker images (pgadmin and PostgreSQL), builds, and runs the containers according to the created yaml file. 
Before you run the command make sure that you defined an `.env` file for your personal environment variables for this project. This `.env`-file has to include the following variables.
```
POSTGRES_USER=root
POSTGRES_PASSWORD=root
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=root
DB_NAME=milestone_3
```
This example is only for localhost setup. If you would like to run code on a public excessible server you have to change these defaults settings and adjust the DB_HOST variable in the `yaml` file.

The program code in the thrid app-container runs the following sequence of actions:
- downloading the training and testing data
- saves the image dataset and their metadata in a Postgre Database
- Trains the CNN based on the training set
- Evaluate the final trained model
- Saves the trained model
- Make predictions on the testing data and save the results also in a PostgreSQL table