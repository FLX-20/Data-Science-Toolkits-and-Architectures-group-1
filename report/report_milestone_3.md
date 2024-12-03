# Milestone 3

## Task 1 - Setting Up Docker Compose








## Task 2 - Simple PostgreSQL Application








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
- The uuid of the image, which serves as a unique identity. The actual image gets the same uuid attached so that the actual image on the volume and the metadata in the database are related to each other.
- The URL gives information where the image and the related dataset come from. A more elegant way to solve this would have been to create a second table for URLs. Each URL can then be associated with one or many images. This is a called one-to-many relationship. In this way, the same URLs would not have been repeated over and over again. However, we try to keep things simple here, so that it keeps understandable for everyone. 
- Moreover, a ground truth label is also stored in the table, which tells the learning and evaluation algorithm what is actually present in the image.
- The last column in the table is the dataset name, which includes the image.

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








