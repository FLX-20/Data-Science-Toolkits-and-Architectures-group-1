# Milestone 2

## 1 Establishing a Clean Git Repository



## 2 Technical Concepts and Tool Preferences



## 3 Building Core Functionality for Model Training and Prediction
## 3.1 Load Datasets
The starting point of loading new datasets for training the model was the [tensorflow documentation for dataloading](https://www.tensorflow.org/tutorials/load_data/images).
The objective was to implement a function that can read datasets from the local filesystem and return the same values as the data loading function for the already included datasets in TensorFlow, such as mnist_fashion or cifrar10. These datasets can be easily loaded with the following functions.
```python
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
```
This objective was defined on our own because the task included too little information. Questions about the data format, the kind of data or the data structure were not clarified. This is why we defined them on our own. 
The dataset has to be already extracted (e.g. unzip) and has to be placed in the `datasets` directory. Inside the directory of each dataset, there has to be a subfolder with the images for every class. 
The Directory structure for the two datasets, which were used to test the code, is presented in the next code block.
```
DATA-SCIENCE-TOOLKITS-AND-ARCHITECTURES-GROUP-1/
├── datasets/
│   ├── Animals/
│   │   ├── cats/
│   │   ├── dogs/
│   │   └── snakes/
│   └── flower_photos/
│       ├── daisy/
│       ├── dandelion/
│       ├── roses/
│       ├── sunflowers/
│       └── tulips/
└── LICENSE.txt
```
These datasets can be installed by executing `download_datasets.sh`. 
In the beginning, downloading the datasets was included in the Python code. However, if you run the code multiple times it is redundant and causes unnecessary computation to download the datasets every time again.
This issue resulted in the decision to exclude this step into a shell script. 


## 4 Code Modularization and Structure Enhancement



## 5 Dependency Management with pip and Virtual Environments



## 6 Containerizing the Application with Docker