# Data-Science-Toolkits-and-Architectures-group-1-

## Project Overview
This repository contains the code and resources for the subject "Data Science Toolkits and Architectures" at the University of Lucerne.
The repository is structured by multiple milestones, with each milestone tackling a specific task, such as running a CNN for image classification using the MNIST dataset.

## Prerequisites
- Python 3.x
- Git
- python packages of the requirements.txt file

## Download the code from the repo
A local copy of the repository can be created with the following command. Make sure that you have installed [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) before.
```shell
git clone https://github.com/FLX-20/Data-Science-Toolkits-and-Architectures-group-1.git
```

## Using a Virtual Environment
We recommend using a virtual Python environment to avoid version conflicts and store the required packages in this new environment. The new virtual environment can be created and activated with this command:
```shell
python3 -m venv env
source env/bin/activate 
```
The required packages are stored in the `requirments.txt` file and can be installed by executing this command.
```shell
pip install -r requirements.txt
```

## Run Milestone 1

From the root of the cloned repository change to folder `milestone_1` and execute the program code of the CNN.
```shell
python3 mnist_convnet.py
```
This folder also includes the tasks and the report of the first milestone,
which explains the CNN python code, how to set up a Linux system for Python development and a simple gut/GitHub workflow.