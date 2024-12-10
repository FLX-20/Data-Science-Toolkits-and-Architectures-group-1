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
The services being used are a python flask application (which is running on port 5000) for the "web" service and a "redis" service that manages the database memory - these communicate using hostnames

### 1.2 Ports being used (application and docker-compose file)
Ports being used are 5000 for the application inside the container and subsequently Docker also exposes the 5000 port to the machine

### 1.3 Computer communicates with the application inside Docker container and the Ports exposed from the application to the host machine
Like this the host communicates with the containerized application via port 5000 - the exposed one. For the redis service, which is based on the official redis image from the Docker hub, port 6379 is used inside the container, meaning it doesn’t expose any ports but is only available within the Docker environment.

### 1.4 Localhost and why it is useful in the domain of web applications
Localhost is refering to the machine´s loopback address, which in this case is 127.0.0.1 . It is useful for accessing and testing applications that run locally, without the need to connect them to external networks, so one can do preliminary testing without (security) vulnerabilities. 



## Task 2 - Simple PostgreSQL Application








## Task 3 - Loading and Saving Images in PostgreSQL Database







## Task 4 - Multi-Docker Container Application








