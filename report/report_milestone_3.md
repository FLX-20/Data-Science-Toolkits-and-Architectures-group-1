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









