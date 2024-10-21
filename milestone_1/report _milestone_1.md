# Data Science Toolkits and Architectures - *Milestone 1*


## 0. Setting up a virtual Machine with Ubuntu

### 0.1 Installing VS Code 
What is VS Code, and how did we installed it? VS Code is a source code editor in which you can open multiple tabs.
Furthermore, VS Code has a build-in support for Git, which will make it easy for us to commit code, 
create branches, and push/pull to our Github repo from VS Code. 
We installed VS Code through the App Center in the Ubuntu server on the Virtual Machine.

### 0.2 Install Python extension in VS Code
First, we need to ensure if Python is already installed on the Linux system.
We use the command 'python3 --version' to see if python3 is already installed.
In the terminal we get an error message that it is not installed so we use 'sudo apt install python3'.
Also we immediately use 'sudo apt update' to update to the latest python version possible which is Python 3.12.0.

### 0.3 Install Git extension in VS Code
To install Git on VS Code we used 'sudo apt install git'. 

### 0.4 Creating a new directory on Ubuntu
Before making a new directory on Ubuntu we first see in which directory we are currently working.
This is done by the command pwd, meaning print working directory.
The new working directory will be called DSTA, referring to the name of the course.
To make this directory we use 'mkdir DSTA'.
If we want to make changes in that directory we use 'cd DSTA' to set our working directory to that folder.
In the terminal we also see now that we are working in the DSTA folder.

### 0.5 Making changes in Git
Eventually we want to make changes that will be visible in our repositorty on Github.
Therefore, we use the command 'git clone' with the link of our repository. So we make changes in git.
Because we want to work in this directory we set 'cd ...' witht the link of our repository. 
We use the 'Tab' button to make our life easier and not type the full link again.
Now the changes will be made for all the files in the current directory.

### 0.6 Open the Git repo to import the Keras code





## 1. MNIST-Dataset

### 1.1 Introduction
First, we decided to read about the dataset in another way, because our browsers notified us about potential security and privacy risks. Our alternative sources were: previous lectures and tutorials, Kaggle, TensorFlow, and Wikipedia for a brief initial overview.

The dataset is about handwritten numbers, or rather their depictions. The data points were aggregated from different official US institutions such as high schools and the US Census Bureau, or rather the hand-filled documents of their students and employees, respectively. This led to differing qualities when it comes to clearness or rather noise in the data points—hence, mixing these "Special Databases," especially 1 and 3, was necessary in order to ensure the derivation of logical conclusions from the empirical evidence.

### 1.2 Objective
The objective of this approach is to enhance efficiency and automate the interpretation of handwritten numbers from a range of handwriting styles. This will improve or rather facilitate machine readability, which is a crucial aspect of many data entry processes. This helps to ensure continuity across media breaks and to lower error rates relative to manual input methods.

### 1.3 Classification Challenge
The fundamental issue that we are confronted with is classification. In particular, we face the challenge of classifying numbers written by hand in greyscale and assigning the corresponding classes (0-9) with the highest possible rate of correctness or rather accuracy.

### 1.4 Dataset Characteristics
The dataset is characterized by depictions of numbers in 28x28 pixel fields. These fields are centered to enhance the probability of accurate recognition. The data files themselves range in size from approximately 4000 bytes to nearly 10 gigabytes, with the training set consisting of almost 60,000 total entries, half of which originate from SD-1 and the other half from SD-3. The test set comprised 10,000 total entries at its outset, with 5,000 patterns derived from SD-1 and 5,000 from SD-3, respectively. 

The authors ensured that the  creators of the entries in the training and test sets were distinct to avoid any overlap or redundancy. This yields a total of 70,000 grayscale images, each with a resolution of 28 by 28 pixels. Each image is represented as a flattened array comprising 784 values (28x28) for each pixel. In other words, the characteristics of each image are represented by the values of the pixels prior to antialiasing. The pixel values range from 0 (black/dark) to 255 (white/bright).


## 2. Checking Git Code Base
We downloaded the python-script from the [github-repo](https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py) and tried to run it on our machines. 
The summary of how to run it is summarized in the README.md file of our repo. The code from the repo is explained in detail in Chapter 5.

## 3. Git and Github workflow
In this chapter we would like to write down our git and github workflow quickly, starting from with an empty folder.

### 3.1 Clone/copy a repository from Github
You can copy a GitHub repository on your machine using the following command.
```shell
git clone https://github.com/FLX-20/Data-Science-Toolkits-and-Architectures-group-1.git
```
It clones/copes all files, commits history and branches from the repository located in the cloud on Git Hub into a new directory on your computer. Thus it creates a local copy of the project.

### 3.2 Creating Branches
If you want to make changes in the repo it is a good habit to create a new branch. It is not recommended that changes be made directly at the main branch. You can create a new branch with the following command.
```
git branch <name_of_branch>
```
Check if the branch was successfully created with the next command, which returns all branches in your current local repo.
```
git branch
```
You can change the branch, in which you are currently working with the next line.
```
git switch <name_of_branch>
```
If you want to delete a branch use the next command.
```
git branch -d <branch_name>
```

### 3.3 Staging and Commiting changes
After the creation of the new branch, you can start making changes and adding new code.

While making changes it is always important to push your stages regularly, so you can jump back if you should have messed something up.

First check the status of the repo to see, which files have been changed.
```
git status
```
Then stage the files, which you want to commit. 
```
git add <file_name>
```
After staging, you can commit your changes to the repository.
```
git commit
```
If you execute the command a window in your default text editor will open. In the first line write down the commit message. Then leave one line out and write a more detailed description of your commit in several sentences and lines, so that everybody can understand what you have done.
After saving the commit messages and closing the editor the changes are committed. 

### 3.4 Pushing and Pulling 
So far we only have made changes to our local system. If we want to save our changes in the GitHub cloud we need to push them. 
```
git push origin <branch_name>
```
In case you are pushing for the first time from a new branch, you can set an upstream branch. Then Git will know which remote branch the local branch tracks, which allows you to push changes only with  `git push`.
```
git push --set-upstream origin <branch-name>
```
The term `origin ' refers to the name of the remote repository. In most cases, when you clone a repository from GitHub, Git automatically names its origin. 

If you know that someone else has made changes to the repository, you should pull the latest version to stay up to date.
```
git pull origin <branch_name>
```

### 3.5 Setting rules in Github
In chapter 3.2 it was already mentioned that working on the main branch is not a good habit. 
Thus, it is important to control exactly what is added to this branch. For this reason, we attached a branch protection rule to this important branch, which prevents unauthorized merges into the main branch. The rule set. This rule enforces an assigned reviewer to approve the changes before the merge is executed. The rule was set up in the following way.
- click on **Settings**
- click on **Bracnches** in the left sidebar
- click on the button **Add branch ruleset**
- enter a name for the rule
- select a target branch (default main branch)
- select **Require a pull request before merging** in button part of the page
- enable the rule at the top part of the page in the dropdown menu **enforcement status**
- click on **create** to apply the rule

## 4. Running Python Code
A summary of how to run the python code of the provided repo is given in the `README.md` of this project. In general a python script is executed in the terminal in the follwoing way.
```shell
python3 script.py
```

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
A Convolutional Neural Network (CNN) is a type of Neural Network, which allows computers to recognize patterns/features in images, such as shapes and objects, by processing small parts of the image at a time. The first CNN was introduced in 1998 by Yann LeCun and hence was called LeNet. It was exactly developed for this task of image classification of the MNIST dataset and is represented in the next image.  
![Convolutional Neural Net](https://d2l.ai/_images/lenet.svg)  
These special types of neural networks are required, because the task of pattern and object detection in images can barely be solved by vanilla fully connected Neural Networks, because they suffer from three problems.  
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

### 5.6 Resources
Of course, it is not possible to explain every detail of NNs, CNNs and the related libraries in such a short report, this is why we provided these links to our sources for further reading.

**Beginner material**
- [But what is a neural network? | Chapter 1, Deep learning](https://www.youtube.com/watch?v=aircAruvnKk)
- [Gradient descent, how neural networks learn | Chapter 2, Deep learning](https://www.youtube.com/watch?v=IHZwWFHWa-w)
- [What is backpropagation really doing? | Chapter 3, Deep learning](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
- [Backpropagation calculus | Chapter 4, Deep learning](https://www.youtube.com/watch?v=tIeHLnjs5U8)

**Advanced Material** 
- [Learning From Data (Yaser S. Abu-Mostafa)](https://amlbook.com/)
- [Dive into Deep Learning](https://d2l.ai/)

## 6. Adding Documentation
The README.md, which is always shown on the first page of the repo, was extended with all important information to run the code of the first milestone. Afterwards, we deleted the repo from our machine and tried to set up a local copy of the repo on our machines following the steps in the documentation. 

## 7. Creating a folder for this milestone
In the folder [milsone_1](https://github.com/FLX-20/Data-Science-Toolkits-and-Architectures-group-1/tree/main/milestone_1), one can find the report of the milestone written in markdown, the pdf-file of the milestone task and the python code of the CNN.
We learnt makrdown with this short [markdowm introduction guide](https://www.markdownguide.org/getting-started/) and [overview page](https://www.markdownguide.org/basic-syntax/).

## 8. Problem in this milestone
The main issue was to set up a functional environment for all team members, enabling them to write code, operate in the terminal, and collaborate effectively.

The initial plan was to run Linux in a virtual Machine for all non-native UNIX users.
However, after setting everything up properly, like it was described in Chapter 0, we came up with the conclusion that our laptops are not able to provide the required resources to work in the virtual environment smoothly without a lack and system crashes.
The two alternative solutions were:
- using Ubuntu directly on our laptops
- using the Ubuntu App on Windows (WSL - Windows-Subsystem für Linux)

In the end, Tjerk started using the Ubuntu APP and Felix uses dual Boot to run both Linux/Ubuntu and Windows on his laptop. 
Tjerk integrated the Ubuntu App terminal into VSCode, by replacing the default Powershell with WSL.
Afterwards, he was also able to run the code that his system crashed.

Another large challenge of this milestone was familiarising Tim and Terjk with Linux, Git/GitHub, working in the terminal and the new coding environment because they never used it before. 

We ended up with the following system configuration for our next milestones.
- Felix: Dual Boot Windows and Ubuntu system (already set up before the course)
- Tim: MacOS (no adjustments required)
- Tjerk VSCode with integrated Ubuntu App terminal (WSL)
Moreover, Terjk and Tim were taught and learned how to get along with the new working environment and tools.

