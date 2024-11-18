# Milestone 2

## 1 Establishing a Clean Git Repository



## 2 Technical Concepts and Tool Preferences



## 3 Building Core Functionality for Model Training and Prediction



## 4 Code Modularization and Structure Enhancement



## 5 Dependency Management with pip and Virtual Environments



## 6 Containerizing the Application with Docker
Docker is an open-source platform for building, testing and deploying applications quickly. It packages software into standardized units, which are called containers. These containers can run consistently across different environments, because they bundle everything that an application requires, such as code, libraries or system tools.
This ensures that everything runs in the same way no matter where it is deployed.  

### 6.1 Installing Docker on our machines
The installation of Docker is more complicated than installing a normal package, for instance over the CLI with apt on Ubuntu.
it is always recommended to follow the newest [Docker Documentation](https://docs.docker.com/desktop/setup/install/linux/ubuntu/) on the offcial Docker webside. 

### 6.2 Creating a Docker file with the necessary dependencies
The task was to create a Dockerfile to build an image. Afterwards, this image can be used to run the code on any machine independent of the operating system.  
We created the Dockerfile manually and didn't use docker-compose, because the Dockerfile of such a small application is short and simple.  
Furthermore, it was a good practice to build the dockefile by hand from scratch. 
If the project becomes more complex we will probably make use of docker compose. 

During the writing of the docker file, the biggest issue was the file itself, but the mounting of the volumes. It took a while to find out how to specify the right paths in the local file system and in the container. 
In the end, three volumes are mounted into the container: datasets, images and models.
These volumes allow the container and the Python code, which runs inside this container to make changes to the filesystem of the local machine.  
It also would have been possible to combine all these directories in one single directory/volume. But in this scenario, the codebase would be nested from our point of view. 

While experimenting with dockerfiles and images. We didn't realize how much space the build images occupy. The result was that after a while almost the entire hard drive was full. This highlights how important it is to delete unused images regularly.
In the worst-case scenario where no disk space was left the following command was executed, which forces removing all containers, volumes, images, and networks. 
```
docker system prune -a --volumes
```
Normally you would use `docker image prune` to delete all `<none>` images and `docker image prune -a` to delete all unused images.
It is also important to note that all containers related to an image need to be stopped to remove it.  
Moreover, we recognize that our final image is quite large with over two 2GB. We think the main reason for this is the installation of the tensorflow library from which we only used a fraction.
A question for the next lecture would be how to decrease the size of this Docker Image.