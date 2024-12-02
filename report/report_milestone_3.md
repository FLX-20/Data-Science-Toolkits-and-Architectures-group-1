# Milestone 3

## Task 1 - Setting Up Docker Compose








## Task 2 - Simple PostgreSQL Application








## Task 3 - Loading and Saving Images in PostgreSQL Database

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


## Task 4 - Multi-Docker Container Application








