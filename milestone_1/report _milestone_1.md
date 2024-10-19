# Data Science Toolkits and Architectures - *Milestone 1*


## 0. Setting up a virtual Machine with Ubuntu

## 1. MNIST-Dataset

## 2. Checking Git Code Base

## 3. Git and Github workflow

## 4. Running Python Code

## 5. Explaining Convolutional Neural Networks
The provided program code in the Git repository is an implementation of a simple **Convolutional Neural Network (CNN)** for image classification, in this case, the classification of the famous **MNIST dataset**, which is introduced in [section 2](##MNIST-Dataset)

### 5.1 Setup part
In the setup section of the code, the required packages are loaded.
```python
import numpy as np
import keras
from keras import layers
```
The first imported library is **NumPy**, a package for scientific computing in Python.   
In the second line, the open-source deep learning library **Keras** is imported, simplifying the process of building deep learning models. Keras started as an independent library. It runs on top of other, more low-level frameworks, such as TensorFlow, Theano, or CNTK. Keras provides the advantage that you can build industry-ready models quickly in fewer lines of code due to its higher abstraction level. In this way, it can be checked quicker if certain neural network architectures can solve the problem.  
Today, Keras is fully integrated into **TensorFlow 2.0**. This allows you to build, try out, and evaluate models quickly with Keras and make finer adjustments with TensorFlow, using its low-level features. The integration also requires the installation of the TensorFlow library. Otherwise, we get the following error when executing the code: 
```shell
ModuleNotFoundError: No module named 'tensorflow'
```
In the last line, the layers module of Keras is imported, which allows different types of layers to be used in the program code.

### 5.2 Data Preparation Part
```python
num_classes = 10
input_shape = (28, 28, 1)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
```
In the subsequent part of the code, the data is prepared and loaded. There are ten classes because the MNIST dataset includes ten different digits from zero to nine. Each grayscale digit image in the dataset has a size of 28 by 28 pixels. Thus, every pixel has a value between 0 (black) and 255 (white). For this reason, the last value in the tuple `input_shape` is 1, because only two dimensions are needed in this case.  
In the last line of the code above, the MNIST dataset is loaded from the Keras library with the [load_data function](https://keras.io/api/datasets/mnist/). he function returns two tuples. One tuple contains the training set with 60,000 images. The other tuple includes the test set with 10,000 images. In the end, the test set is used after training the model to evaluate the built and trained neural network. All these 70,000 images in both datasets are saved as NumPy arrays, which allow for more efficient calculations.
```python
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
```
In the following part of the data preparation, the pixel values of the images are normalized. The division by 255 scales each integer pixel value from a range between 0 and 255 to a range between 0 and 1. Before this calculation, the data type of each pixel is changed from an integer to a floating-point data type. Without this explicit data type conversion, Python would automatically do an implicit data type conversion into a float64. This data type uses 64 bits to represent floating-point numbers, which is twice as much as the suggested method in the code. These normalizations improve convergence speed, avoid overflows in calculations, and are more suitable for activation functions like sigmoid or ReLU.  
In the next code block, an extra dimension is added to the input images of the training and test sets with the help of the [expand_dims](https://numpy.org/doc/2.0/reference/generated/numpy.expand_dims.html) function. This is necessary because many deep learning models require a parameter that defines the channel dimension. In this case, the channel dimension is one, because grayscale images only have one channel. If we were dealing with RGB images, we would have three channels.
```python
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")
```
After preparing the input data, the final shape of the training input tuple `x_train` is printed out. It shows `(60000, 28, 28, 1)` as the shape output, meaning it includes 60,000 images with a height and a width of 28 pixels and 1 channel.
Afterward, the number of test and training images is printed out. In the dataset, there are 60,000 training and 10,000 test samples.
```python
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
```
So far, we have only prepared the images, which are ingested into the neural network. But to train the neural network, labels are also required because we are dealing with a supervised learning task. The labels of the images are stored in the `y_train` and `y_test` datasets. In the beginning, these labels are stored as integer values referring to the appropriate class. Computation speed can be increased by converting these integer values into categorical values, which should be predicted by the neural network. Exactly this is done in the above code block with the [`to_categorical()`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical) function.

### 5.3 Building the Model 
After the preparation of the data, the model is created. But before diving deeper into model in this code we need to gain an understanding how Neural Networks in general work.

#### 5.3.1 How does a Neural Network work?
A fully connected vanilla neural network is a combination of several layers of perceptrons stacked on top of each other. 
A perceptron can be understood as a linear threshold unit. If the weighted sum of an input vector exceeds a certain threshold 1 is returned otherwise 0. 
A visualization with an equation is shown in the next figure.
![Perceptron](https://www.nomidl.com/wp-content/uploads/2022/04/image-5.png)  
The supervised training algorithm of the perceptron can be used to separate any binary, linear separable dataset.
In this training phase the weights $w_n$ are learned to separate the two classes from each other. 
However, the perceptron learning algorithm will never converge for no linear separable data, which can occur quite often in the real world.
One solution for the problem is Neural Networks, which we discuss in this report.
The Universal approximation theorem states, that a simple neural network with only one hidden layer, like in the next figure, is able to approximate any given continuous function in a finite interval. 
This approximation increases with the number of perceptrons/neurons in this layer. 
Moreover, the activation function has to be non-linear, because the composition of many linear functions remains a linear function, but non-linearity is needed to approximate any function.  
We refer to the term deep neural network as to network with many hidden layers, which are responsible for detecting different features in the data.  
![Simple NN & Deep NN](https://www.dilepix.com/hs-fs/hubfs/schema-neural-network.png?width=728&name=schema-neural-network.png)  
After getting an idea of the strucuture of the Neural Network, we continue understanding the training process better.
This process can be split into two parts:
- **foreward propagation:** The input is passed from the input layer to the output layer through the entire network with its nodes and activation functions.
- **backward propagation:** In the end the of the foreward propagation process the error is calculated. This error is then backpropagated through the network. The purpose of backpropagation is to compute the gradient of the loss function with respect to each weight in the network.  

The overarching goal of the network during the learning phase is to decrease the final error by adjusting incremantly adjusting the weights of the network.   

#### 5.3.2 What is a Convolutional Neural Network?
A Convolutional Neural Network (CNN) is a type of Neural Network, which allows computers to recognize patterns/features in images, such as shapes and objects, by processing small parts of the image at a time. The first CNN was introduced in 1998 by Yann LeCun and hence was called LeNet. It was exactly developed for this task of image classification of the MNIST dataset. These special types of neural networks are required, because the task of pattern and object detection in images can barely be solved by vanilla fully connected Neural Networks, because they suffer from three problems.  
- **Large Number of weights:** If every pixel of an image is treated as an input, you end up with a large number of weights. An input image of the size 28x28 would result in 784 weights per node for each node in the first hidden layer. This requires too much computation to update all weights during backpropagation and thus scales terribly with the size of the image.
- **Not resistant against shifts:** If the objects or patterns in the test images are shifted by a few pixels compared to the images in the training set, the objects inside the images might not be recognizable anymore for the NN. 
- **Correlation between the pixels is not taken into accout:** There is a high probability that the pixel, which is surrounded by white pixels is also white or close to pure white.
CNNs provide a remedy for these problems by reducing the number of input nodes of the final fully connected.

The process of convolution in images is represented in the following image.   
![convolutional filter example 1](/milestone_1/images/convolution_filter_example_1.jpeg)
![convolutional filter example 2](/milestone_1/images/convolution_filter_example_2.jpeg)

The CNN finds the appropriate weights/values for the kernels that are used in the convolution process on its own via backpropagation.
In the past, scientists manually developed kernels to detect image patterns, for instance, with kernels for edge detection. Nowadays, convolutional neural networks can find kernels that provide far better results.

## 5.3.3 Explanation of the CNN code
Now, after explaining shortly the idea for NN and CNN, we will continue going through the code.
```python
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()
```
The [`Sequential()`](https://keras.io/guides/sequential_model/) function provides a simple way to build a neural network layer by layer. The name sequential comes from the design principle that the layers are stacked one after another. The constructor/function takes a list as an input, describing the structure of the neural network, and returns a sequential model object.    
The first defined layer in the list is the input layer. It describes the input of the network. The input shape was determined at the beginning of the code in `input_shape`.  
The consecutive layers are a stack of convolutional layers, max-pooling layers, and the non-linear ReLU activation function, which gives convolutional neural networks their capability to detect patterns and objects in images.   
- **Convolutional layers**: Detect features within the images.
- **Pooling layers**: Reduce the spatial dimensions of the data.
- **Flatten layer**: Converts the 2D matrix data into a vector.
- **Dropout layer**: Prevents overfitting by randomly dropping units during training
- **Dense layer**: Fully connected layer for output prediction using the softmax   activation function. 

All these layers were already summarized in the image above, showing a convolutional filter example. The only new thing is the dropout part. Dropout is a type of regularizer, which randomly drops/leaves out neurons in the training process. Each neuron is retained with a probability of p. Halff of the fully connected network is dropped out while training. This improves the CNN's performance to also classify unseen data with high accuracy after training because the network relies more on the presence of certain neurons.  

### 5.4 Train the model
After defining the strucuture of the model the trainig phase can be started.
```python
batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
```

Before the training process is started two variables are initialized. 
- The **batch size** defines the number of samples/images that the model will process before updating the weights.
- The number of **epochs** defines how many times the model goes through the entire training set.

The method `compile` prepares the model of training by setting the loss function, the optimizer and the metrics, that should be tracked while training.
- The categorical cross-entropy loss is commonly used for classification problems. It measures how far off the prediction is from the true value. The error is then backpropagated through the CNN. In the case of a regression problem, the mean squared error is a common choice as a loss function.
- The optimizer describes how the parameters/weights during backpropagation are updated. The [Adam](https://arxiv.org/abs/1412.6980) optimizer is a common choice, which works best in many cases. 

Finally, in the last line, the model is trained based on the setting before, using the `fit` method.

### 5.5 Evaluating the model
At the end of the code, the built and trained model is evaluated with the unseen test data. This can be done with the `evaluate()` method of Keras. This method returns a list with two values. The first value is the test loss. The second value is the test accuracy.
$$
Accuracy = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}
$$
While accuracy measures how often the model makes the correct prediction, loss measures how far the predictions are from the true values.
A small loss and a high accuracy give evidence of a well-trained model, if the dataset is balanced.
```python
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
```

## 6. Adding Documentation

## 7. Creating a folder for this milestone

