# Milestone 2

## 1 Establishing a Clean Git Repository



## 2 Technical Concepts and Tool Preferences



## 3 Building Core Functionality for Model Training and Prediction



## 4 Code Modularization and Structure Enhancement



## 5 Dependency Management with pip and Virtual Environments

### 5.1 traditional Virtual Environment and Dependency Management
In Python, virtual environments are necessary to separate project-required dependencies from system-wide packages. This avoids conflicts between packages. 
A virtual environment can be created and activated with the following commands.
```shell
python -m venv venv
source venv/bin/activate
```
You can check if `venv` was successfully created with `which pip`. 
After the change of the environment, all newly installed packages are stored in this `venv`. 
The simplest way to create a `requirements.txt` is to use `pip freeze` to list all installed packages and their version and pip them into the `requirements.txt` file.
```shell
pip freeze > requirements.txt
```
After the creation of this file, it can be used by other people to quickly install all required packages at once in their virtual environment to run the code.
```shell
pip install -r requirements.txt
```


## 6 Containerizing the Application with Docker