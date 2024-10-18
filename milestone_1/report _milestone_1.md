# Data Science Toolkits and Architectures - *Milestone 1*


## 0. Setting up a virtual Machine with Ubuntu

## 1. MNIST-Dataset

## 2. Checking Git Code Base

## 3. Git and Github workflow

## 4. Running Python Code

## 5. Explaining Convolutional Neural Networks
The provided program code in the Git repository is an implementation of a simple **Convolutional Neural Network (CNN)** for image classification, in this case, the classification of the famous **MNIST dataset**, which is introduced in [section 2](##MNIST-Dataset)

### 6.1 Setup part
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

## 6. Adding Documentation

## 7. Creating a folder for this milestone

