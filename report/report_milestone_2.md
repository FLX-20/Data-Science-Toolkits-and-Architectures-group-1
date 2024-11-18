# Milestone 2

## 1 Establishing a Clean Git Repository



## 2 Technical Concepts and Tool Preferences



## 3 Building Core Functionality for Model Training and Prediction



## 4 Code Modularization and Structure Enhancement



## 5 Dependency Management with pip and Virtual Environments



## 6 Containerizing the Application with Docker
At this exercise Dockerize our code

### 6.1 Installing Docker on our machines
We installed [Docker] https://docs.docker.com/engine/install/ for Windows and IOS on the original Docker website.

### 6.2 Creating a Docker file with the necessary dependencies
We have used the code `docker build -t tensorflow-cpu-app .` in a new terminal to build the Docker Image. Only I got an error that there is no dockerfile in my directory. Because I forgot to make a dockerfile. Therefore, I made a new file, calling it Dockerfile. In this Dockerfile I added the following lines
```
# Use an official TensorFlow Docker image (CPU version)
FROM tensorflow/tensorflow:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory for saving models
RUN mkdir -p /app/saved_models

# Command to run the script (replace "main.py" with your actual Python script)
CMD ["python", "src/main.py"]
```
Then I executed this command `docker build -t tensorflow-cpu-app .` in my terminal again. It worked but it took 7 minutes to finish. 

