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




## Task 4 - Multi-Docker Container Application








