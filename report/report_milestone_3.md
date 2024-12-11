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

a) What is PostgreSQL? SQL or NoSQL
It is a RDBMS, which is short for relational database management system - it uses SQL, which is short for structured query language to access, define and manipulate data. Furthermore the ACID structure, referring to the data points being Atomic, Consistent, Isolated and Durable is another sign for the SQL nature of PosegreSQL. As such it is SQL as the data is stored in a structured way in tables with rows and columns and Primary as well as Foreign Keys are utilized.

b) If the container was stopped  and started again the joke would still be in the Database, yes, because the data memory is not-volatile, meaning it can persist through restarts or even power outtages. This means that the joke will still persist, as it does after one has used "stop" and "start" commands to restart the container, because docker volumes remain even after the corresponding container stops. 






## Task 3 - Loading and Saving Images in PostgreSQL Database

### 3.0 Intorduction of impedance mismatch and object relational mappers

#### Impedance Mismatch
An impedance mismatch in computer science refers to the conflict,
which arises when two systems represent the same data in fundamentally different ways.
In software engineering, this term is commonly associated with object-relational impedance mismatch.
This term describes the issue of mapping data between object-oriented programming (OOP) to relational databases.
The problem is that OOP structures its data hierarchically in nested objects. 
On the other hand, relational databases have tables with explicit relationships, such as one-to-many.

#### Object Relational Mappers
These are tools, which bridge object-oriented programming (OOP) and relational databases. 
Two popular ORM Frameworks in Python are SQLAlchemy and Django ORM. 
So far we don't use non of them, but we will switch to SQLAlchemy as soon as we start to build our Flask Web Application.
We executed the SQL queries as required in the second task, using `psycopg2` as a PostgreSQL adapter to perform our queries.

#### Impedance Mismatch in our Project
In our Project, we don't have a classical impedance mismatch, because our code is not directly written in an object-oriented programming manner by us.
It involves the use of classes, methods, and attributes through the imported libraries. 
However, we have not yet defined any classes or constructors ourselves.
Hence, our code can be referred to as procedural programming, which performs its steps sequentially.  
Thus, the impedance mismatch arises less from the way how the code represents data, but from the actual datatype, 
because images are not stored in a relational database naturally.  
However, if images have to be stored in a relational database, the BLOB data type is often used (Binary Large Object).
This also applies to the processing of audio and video files. 
Many databases, including SQL and MySQL, support the BLOB data type. 
However, PostgreSQL does not offer BLOBs. Instead, it uses the BYTEA data type to handle binary data. 
It's important to note that BYTEA is not the best option for storing very large data, 
as it has a maximum size limit of 1 GB per column.  
For all these reasons, we decided to only store the metadata of the images in our PostgreSQL database 
and exclude the images on a Docker volume, which is closely explained in the following chapters.


### 3.1 Downloading Datasets
Since the last milestone 2, we haven't used the default MNIST Dataset anymore.
We developed the `download_and_extract_zip()` function, which downloads, unzips and saves the dataset from the web.
If the code is executed a dataset from Kaggle about cats, dogs and snakes is downloaded.
In the end, this function could handle any dataset. The only prerequisite in our code is that the subdirectories in the downloaded and unzipped folders have to be the subdirectories of the categories for the classification problem. This structure is visualized in the next code block.

```
project_directory/
│
├── data/
│   ├── cats/
│   │   ├── cat1.jpg
│   │   ├── cat2.jpg
│   │   └── ...
│   ├── dogs/
│   │   ├── dog1.jpg
│   │   ├── dog2.jpg
│   │   └── ...
│   ├── snakes/
│   │   ├── snake1.jpg
│   │   ├── snake2.jpg
│   │   └── ...

```
Some datasets on Kaggle are divided into training, testing and validation. Datasets in this form are not appropriate for our `download_and_extract_zip()` function. Thus we don't cover every edge case of how training datasets are represented.
However, if a dataset, which should be used for training is not in the appropriate format by default, there is still the possibility
to save the data on your own on a public cloud in the right structure and download it from there.

### 3.2 Relational Database 
We decided to store only the metadata in the relational database. Hence the images are not stored directly in the database, but on a docker volume, where the docker container can access them. 
This decision was made because Relational Databases are not designed for storing images. It is possible but not common in practice. If it should be really required to store the images in the database, the code for this can be found on [geeksforgeeks](https://www.geeksforgeeks.org/save-a-image-file-on-a-postgres-database-python/), which can be easily copied, pasted and adjusted to the needs.  
The stored metadata in our database includes:
1) The **uuid** of the image serves as primary key (unique identity). The actual image gets the same uuid attached so that the actual image on the volume and the metadata in the database are related to each other.
2) The **URL** is stored as a string and gives information where the image and the related dataset come from. A more elegant way to solve this would have been to create a second table for URLs. Each URL can then be associated with one or many images. This is a called one-to-many relationship. In this way, the same URLs would not have been repeated over and over again. However, we try to keep things simple here, so that it keeps understandable for everyone. 
3) Moreover, a ground truth **label** is also stored as a string in the table.It tells the learning and evaluation algorithm what is actually present in the image.
4) We also included the dataset name to which the image belongs. This allows you to store images for several different CNNs in the same database, because you can query for the desired image.
5) The last column of the table indicates whether the image is designated for **training or testing**, based on the saved boolean value. This division is performed in the `split_data_into_training_and_testing()` function. Saving this feature in the database allows us to change it in SQL code directly not only in python

This structure allows to store several different training datasets in the same table.  
The final extracted images are stored in a docker volume in a directory with the name of the dataset. Now all images of the training dataset are stored in the same directory. There is no division in subdirectories necessary anymore because the images are renamed by their uuid and the metadata in the relational database provides all other necessary information. 

Moreover, this structure allows us to select rows by their label with the following query.
```SQL
SELECT * 
FROM images
WHERE label = 'snake';
```
The same approach can be applied to select images from a specific dataset if more datasets are added to the `image` table in the future.
```SQL
SELECT * 
FROM images
WHERE dataset_name = 'Animal';
```

## Task 4 - Multi-Docker Container Application








