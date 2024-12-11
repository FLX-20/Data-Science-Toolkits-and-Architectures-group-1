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
## Little project riddles (optional)

## 4.4 Creating Database Table
In the task it was requested to create two tables in our database. One table for the actual metadata of the images and a second table for their prediction.
The first table is created by the function `create_table()`. The second table is created by the function `create_predictions_table()`.  
The queries defined in both functions are executed by the `execute_query()` to not repeat our self. This function createa connection to the database and executes the given query.
The required configuration to connected to the database are defined in the file `db_config.py`, which loads the defined environment variables with [dotenv](https://pypi.org/project/python-dotenv/). Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.  
The newly introduced image_predictions table records the predictions made for various iamges, including details such as the predicted labels, the model used, and the timestamps of those predictions. In contrast, the images table contains information about individual images, including their URLs, labels, and associated dataset names. There exists a one-to-many relationship between each image in the `images` table and multiple related predictions in the `image_predictions` table. This design choice was made to allow several prediction for the same image from different models. 
### 1. SQL Injection Attack
An SQL Injection attack happens when hackers trick your website into running harmful code in the database by typing 
unexpected inputs, like special characters or commands, into fields like login forms. This could let them steal 
data, bypass login, or even delete important information.

## 4.5 Loading Images to the Database
Immediately after downloading and unzipping new data from the Internet its metadata is added to the database and all images are moved into one directory with the defined name of the dataset.
All this is done in the `download_and_prepare_dataset()` function, which hands over the smaller tasks to specialized functions, such as:
- `download_zip()` downloads and unzips the data from the provided URL
- `extract_zip()` extracts the previously downloaded zip file
- `process_and_store_files()` renames the files with their uuid and inserts their metadata into the database
- `split_data_into_training_and_testing()` updates the boolean column `is_training`, which is by default true, based on the defined train test split, for instance, 80% training data and 20% testing data.
#### An example of a SQL Injection Attack:
SELECT * FROM users WHERE username = 'user' AND password = 'pass';

## 4.6 Loading images from the Database
For training the metadata and the images themselves need to be loaded again. This is achieved by the implementation of some new functions.
The function `get_uuids(is_training=True)` returns the uuids of all training or testing images from the database based on the boolean value.
Afterwards, these uuids can be used by `load_images_and_labels_by_uuids()` function to load the image from the docker volume and their related ground truth labels from the database.
The subsequent training process did not change compared to the previous milestones.
The same function only with different parameters where applied for testing. In this case `is_training` was set to False in the `get_uuids` function.
If a hacker enters `user' OR '1'='1` as the username, the query becomes:
SELECT * FROM users WHERE username = 'user' OR '1'='1';

## 4.7 Classifying images
A part, which was newly added to this milestone is the `classify_image_func()`. This function loads the test images and uses the previously trained model to predict their labels
and store these results in the `image_predictions ` table of the database.  
The biggest challenge in this part was to get the actual label names because the `load_images_and_labels_by_uuids()` returns only the encoded labels for training and testing.
This problem was solved with the following two lines of code.
```python
label_names = sorted({row[2] for row in get_metadata_by_uuids(testing_uuids)})
predicted_labels = [label_names[idx] for idx in predicted_indices]
```
These two lines of code translate predicted labels (0,1,2) into human-readable labels (cats, dogs, snakes). First, it extracts all unique labels from the label column of the image table obtained through the `get_metadata_by_uuids()` function. These unique labels are then sorted alphabetically to create a consistent order, resulting in the label_names list.  
In the next step, the code maps each predicted index from the predicted_indices list to its corresponding label in label_names. This mapping produces a list of predicted_labels, where each index is replaced by the appropriate human-readable label.
Then these results can be stored in the `image_predictions` table of the database.
This always returns true, letting them log in without the right password.

#### How to protect yourself against a SQL Injection Attack
1. Use Safe Query Methods:
   cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, password))
2. Check Inputs: Make sure inputs only allow expected characters (e.g., no `--` or `'`).
3. Restrict Database Access: The website’s database account should only have limited permissions.
4. Test for Vulnerabilities: Regularly check for weaknesses using tools like SQLmap.



### 2. Difference Between Relational Database (RD) and a Document Store (DS)

#### Relational Database:
Relational Database stores data in `tables` with rows and columns, like a spreadsheet. It has a fixed structure, so the data must fit a specific format (e.g., numbers, dates). Examples of RD are MySQL or PostgreSQL.

#### Document Store:
Document store stores data as `documents`, like JSON files. Each document can look different. It is very 
flexible, so you do not need a strict structure. This is great for unstructured or changing data. Examples of DS are MongoDB or CouchDB.

#### 2.1 Scenarios Where You Should Use Relational Database:
You should use RD when data is highly structured, and relationships matter, like in finance, 
healthcare, or HR systems where you need consistency and complex queries.

#### 2.2 Scenarios Where You Should Use Document Store:
You should use DS when data is less structured or needs flexibility, such as handling product catalogs, 
user profiles, or social media posts where schema might change frequently.

### 3. SQL Join Operation
A SQL Join combines data from two or more tables when they have a common link. Same as merging two datasets with
one common column variable. 

#### Types of Joins + Examples:
1. **INNER JOIN**: Only shows matching data from both tables.
   SELECT employees.name, departments.name
   FROM employees
   INNER JOIN departments ON employees.dept_id = departments.id;

2. **LEFT JOIN**: Shows everything from the first table and matches from the second table (or `null` if there’s no match).
   SELECT employees.name, departments.name
   FROM employees
   LEFT JOIN departments ON employees.dept_id = departments.id;

3. **RIGHT JOIN**: Opposite of LEFT JOIN—shows all data from the second table and matches from the first table.
   SELECT employees.name, departments.name
   FROM employees
   RIGHT JOIN departments ON employees.dept_id = departments.id;
