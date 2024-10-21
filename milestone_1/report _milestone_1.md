# Data Science Toolkits and Architectures - *Milestone 1*


## 0. Setting up a virtual Machine with Ubuntu

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

## 3. Git and Github workflow

## 4. Running Python Code

## 5. Explaining Convolutional Neural Networks

## 6. Adding Documentation

## 7. Creating a folder for this milestone

