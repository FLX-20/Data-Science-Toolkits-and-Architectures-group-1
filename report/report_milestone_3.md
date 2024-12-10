# Milestone 3

## Task 1 - Setting Up Docker Compose

We installed the docker-compose and got through the 
[tutorial] (https://docs.docker.com/compose/gettingstarted/).
We followed the instructions in the tutorial, creating a new directory called `composetest`. Within that folder we 
created the files: `app.py` `compose.yaml` `Dockerfile` `infra.yaml` `requirements.txt` and plugged that text in 
that was needed. The commands `docker compose up` was needed to run and start the application. To control if the 
application was running we entered `http://localhost:8000/`. This command gave the result: `Hello World! I have 
been seen 1 times.`, when refreshing the page the 1 changed into 2 The second command gave the result: `Hello 
World! I have been seen 1 times.`, when refreshing the page the 1 changed into 2. This was no surpise because we 
wrote `return f'Hello from Docker! I have been seen {count} times.\n'` in the app.py file. When we completed step 8 
we used the command `docker compose stop` to bring everything down and remove all the containers, ending the 
tutorial.


### 1.1 Services used for application and how they relate to host names in computer networks

### 1.2 Ports being used (application and docker-compose file)

### 1.3.1 Computer communicates with the application inside Docker container

### 1.3.2 Ports exposed from the application to the host machine

### 1.4 Localhost and why it is useful in the domain of web applications




## Task 2 - Simple PostgreSQL Application








## Task 3 - Loading and Saving Images in PostgreSQL Database







## Task 4 - Multi-Docker Container Application








