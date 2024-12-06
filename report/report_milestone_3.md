# Milestone 3

## Task 1 - Setting Up Docker Compose








## Task 2 - Simple PostgreSQL Application








## Task 3 - Loading and Saving Images in PostgreSQL Database







## Task 4 - Multi-Docker Container Application

### 4.1 PostgreSQL Container
It PostgreSQL Database runs in its own container. This container is called `postgre_conatainer` for easier identification. This container uses the latest PostgreSQL image, which is downloaded from Dockerhub. 
Moreover, we defined that the container should be restarted automatically if there should be a crash.  
Afterwards, we set the environment variables, which are loaded from the host system.
We don't write out these variables (POSTGRE_USER, POSTGRE_PASSWORD, POSTGRE_DB) in plain text, because these are sensitive information, which should not be published on GitHub, even so, our application only runs locally so far.  
In the next step, we created a volume ensuring the database data persists even if the container is restarted or removed.  
At the end of the container definition, the port for external connections is specified, and the `app_network` is included. Currently, this network is not necessary because there is only one Docker Compose file in this project, meaning there is no need to isolate services from one another. The inclusion of this network was mainly made with future milestones and sprints in mind.

### 4.2 pgAdmin Container
The next container is the docker-compose file for the pgAdmin Service. pgAdmin is a web-based graphical user interface (GUI) tool for managing and interacting with PostgreSQL databases. We called it `pgadmin4_container for identification.  
For the container, we used the latest pgadmin4 image from dockerhub.  
Like the PostgreSQL container. The pgAdmin container also restarts in case of a crash automatically. 
The environment variables (PGADMIN_DEFAULT_EMAIL, PGADMIN_DEFAULT_PASSWORD) are also not stored in plain text in the yml file but are loaded from the host system.  
We also defined here a volume to save the pgAdmin configurations.  
In the next step, port 5050 on the host is mapped to 80 in the container. This allows us to access pgAdmin through the web browser via this URL `http://localhost:5050`  
Furthermore, it is important to define in the `depends_on` section that the database should start before pgAdmin.

## 4.3. Application Container
In the last container with the name `app_container` our code is executed. 
It builds our defined `Dockerfile`, which lies in the same directory.   
This file has not changed much to the previous milestone. We enhance the container rebuilding performance by installing the TensorFlow image prior to all other dependencies. Additionally, we increased the `--default-timeout` settings, as the building process frequently encountered interruptions due to excessive duration.  
In the final step, we adjusted the `CMD` to allow us to run our entire application with a single command. This includes everything from training and testing to image classification. Now, you only need to execute `docker-compose up` to run the entire application at once.
We also defined environment variables for the application container (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT), which are required for the database connection.  
In the next step, we mounted the entire current directory (.) into the container at `/app`, allowing code changes to be reflected without rebuilding the image.
This might not be recommended for production, but is in the dvelopment process quite practical and saves time. 
It is also important to ensure that this container does not start before the database, as there would be no database to connect to.

## 4.4 Creating Database Table
In the task it was requested to create two tables in our database. One table for the actual metadata of the images and a second table for their prediction.
The first table is created by the function `create_table()`. The second table is created by the function `create_predictions_table()`.  
The queries defined in both functions are executed by the `execute_query()` to not repeat our self. This function createa connection to the database and executes the given query.
The required configuration to connected to the database are defined in the file `db_config.py`, which loads the defined environment variables with [dotenv](https://pypi.org/project/python-dotenv/). Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.  
The newly introduced image_predictions table records the predictions made for various iamges, including details such as the predicted labels, the model used, and the timestamps of those predictions. In contrast, the images table contains information about individual images, including their URLs, labels, and associated dataset names. There exists a one-to-many relationship between each image in the `images` table and multiple related predictions in the `image_predictions` table. This design choice was made to allow several prediction for the same image from different models. 





