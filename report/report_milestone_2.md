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

## 3.2 Training the Neural Network
The Convolutional Neural Network can be trained by executing the following command after building the docker image.
```
docker run --rm \
 -v ./images:/app/images \
 -v ./datasets:/app/datasets \
 -v ./models:/app/models simple_cnn \
 --mode train \
 --dataset_path /app/datasets/Animals \
 --model_file_path /app/models/cnn_model.keras \
 --batch_size 64 \
 --epochs 20
```
This version of the code uses a parser to modify some of the inputs such as the `dataset_path`, `model_file_path`, `batch_size` and `epochs` via the CLI, instead of storing them in an additional config file. This makes it possible to run the code quickly with different datasets or batch sizes.    
The actual structure of the CNN and the related training process was not changed in this milestone, because we assume that this is part of the next milestone. 
Thus, the final model accuracy and the confusion matrix for both datasets are not optimal and much space for further improvement. 

## 3.3 Saving the Model
After the model training the model is saved as a `.h5` or `.keras` file in the model's directory, which is created by the download_datasets.sh script. The decision to provide both file types came from the note in the documentation that the `.h5` filetype is deprecated and the newer version `.keras` is recommended.  
If the file ending provided via the parser is neither `.h5` nor `.keras` an error message is printed out.  
It is also important to mention that we are aware that not all edge cases for inputs via the parser are modelled out. This could be improved in the future by better exception handling to improve the stability and robustness of the code. 
As long as this is not the case the code should be exactly executed how it is described in the `README.md`.

## 4 Code Modularization and Structure Enhancement



## 5 Dependency Management with pip and Virtual Environments



## 6 Containerizing the Application with Docker