# Milestone 4

## Task 1 - Evaluation Metrics and Weights and Biases
First, we all made an account at Weights and Biases [website] (https://www.wandb.com/).
Afterwards, we completed the tutorial on [GoogleColab] (https://colab.research.google.com/drive/1pMcNYctQpRoBKD5Z0iXeFWQD8hIDgzCV)

### 1.1 Experiment Management and its importance
Experiment management is the act of systematically tracking and documenting the learning and progress of your experiments.
It allows you (the researcher) and others to understand what has been done, what results it has produced or is producing,
and to trace exactly where changes have been made and what the consequences are. This ensures reproducibility and robustness
by tracking code versions and the respective datasets used. It also allows comparison and collaboration between teams and 
experiments, since every step or design choice can be examined in detail (by any member who has access to the experiment management database).

### 1.2 Metric in ML
Metrics are key figures or parameters that can be measured and interpreted. They allow us to quantify impact,
so we can judge not only how absolutely good or bad a metric is at any given time, but also in which direction 
it is trending. In other words, metrics allow us to identify and evaluate trends over time.

In the context of machine learning, metrics are particularly important because they provide a way to evaluate
the performance of the models being used. For example, certain metrics can show how many instances have been
correctly identified out of the total number of observations - this is known as the 'accuracy' metric. 
Similar metrics, which will be explored in more detail in the next step, help to provide a more comprehensive understanding of model performance.

### 1.3 Precision and Recall, the trade-off between the two
Precision and recall are probably the most common and popular metrics used in machine learning. 
While Precision focuses on how often we get it right when predicting something to be positive, 
Recall focuses on how often we correctly identify positives out of all the actual positive instances
(so even when we, incorrectly, predict something to be negative).
Precision is about how many times your positive predictions are correct. 
For example, if your model says that 10 emails are spam while 8 of them are spam, 
then you have an 80% precision.
Recall is about how many of the actual positive cases your model found. If there were
20 spam emails and your model only flagged 8, your recall is 40%.
The trade-off between them arises because increasing Precision often decreases Recall and vice versa - like a seesaw,
as one side or metric goes up, the other tends to go down. For example, if a model is designed to prioritise Precision,
it will only predict something as positive only if it's very confident to be right, this will lead to potentially 
missing some real positives (lower Recall). On the other hand, if the model prioritises Recall,
it may predict more positives overall, leading to more false positives and therefore lower Precision.
In the example of cancer diagnostics: Trading off Precision, how often we actually, correctly, 
predict a patient to have cancer, will lead to some patients with cancer not being flagged. 
On the other hand, prioritizing Recall ensures that nearly all patients with cancer are flagged, 
but this may result in a higher number of false positives.


### 1.4 AUROC Metric
The AUROC metric, which stands for “Area Under the Receiver Operating Characteristic Curve", 
quantifies how good a model is at classification tasks, between two classes. Thus allowing to quickly assess the false
positive rate that is associated with a true positive rate. The formula plots Recall against the so called “False Positive Rate” 
at the varying classification thresholds set. Like this, AUROC as a metric gives insight into how well the respective model(s) 
are at classifying the data points at hand. As in regression, a higher value is generally indicating a better fit,
with 1.0 examplifying a perfect distinction of all data classes. What makes AUROC so useful is in areas where data sets tend
to be skewed toward 1 data class that is outweighing all others - here accuracy could be high, even if the model only ever 
predicted that specific class, due to its prevalence - but AUROC allows all class separations to be taken into account and 
thus gives a more differentiated perspective.

### 1.5 Confusion Matrix
A confusion matrix is a table that breaks down how well your model did in a classification problem. The table shows
True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN)
TP is when the model correctly predicts something positive. TN is when the model correctly predicts something as negative. 
FP is when the model says something is positive, while it is not. FN is when the model misses a positive case. 
The confusion matrix is useful because it lets you calculate all sorts of metrics like precision, recall, accuracy,
and gives you a clearer picture of where your model is messing up. 
Therefore, the confusion matrix can be used to measure precision and recall.
Precision is calculated through: 
`Precision = TP / (TP + FP)`
This shows how often the model's positive predictions are correct.
Recall can be calculated through: 
`Recall = TP / (TP + FN)`
This shows how many actual positives the model manages to find.





## Task 2 - Improving Model Performance

After a `Weights and Biases` account had been created, the existing codebase was instrumented with `Weights and Biases` features.  This was achieved by adding a new operational mode, besides, `download_data`, `train`, `test` and `all`. This mode is `wandb_run`, which builds several models defined in a JSON file and transmits the results to the Weights and Biases server. In this way, one can evaluate the models in the related web-application.

### 2.1 Login to W&B
The API key is used to log in to `W&B`. This key is saved in the `.env` file, which is stored only locally on the host machine and is not shared on the remote GitHub repo. Hence, if you want to run the code, you have to enter your own `W&B` key to access the results in the web application.  
The API-key is added as a environment varaible of the docker container by adding it to the `environment` section of the docker-compose file. Docker-compose reads in automattically all required variables form the `.env`-file and adds them as environement variables in the `app` container.

### 2.2 Model Training
Before the model can be trained the CNN architecture has to be loaded from the regarding JSON file.  
This code architecture, incorporating the reading from a JSON, was chosen to run several CNN model tests in a sequence. Because the code is not hard coded, it will be easier in the future to try out different hyperparameter combinations of CNNs, making it easier to find an appropriate model.  
Before the model can be trained the cnn arichtecture have to be loaded from the regarding json file.
This code architcture incoperating the reading from a json-file was choosen to run several cnn models test in a sequence, which will make it easier in the future to try out different hyperparameter combinations, because the code is not hard coded.
After the model was build with the `build_model_wandb` function it is trained in the subseqent step.
Normally one wourd you the [Adam](https://arxiv.org/abs/1412.6980) (Adaptive Momentum Estimation) optimizer for updating the weights in the neural network. But Stochastic Gradient Descent was also added as an option. However, it is not assumed that SGD adds better results, because Adam-optimized is an improved version of SGD, which also combines momentum optimization and RMSP (Root Mean Squared Propagation) to achieve better convergence. Momentum helps accelerate gradients in the right direction by averaging past gradients, while RMSProp adjusts the learning rate for each parameter based on a running average of recent gradient magnitudes, preventing oscillations.  
Nowadays, the Adam optimizer is used in most of the papers, because it achieves so far the best results in many situations. From my own experience, it can be said, that the optimizer does seem to have a tremendous influence. Larger performance boosts can be achieved with other hyperparameters. 
The used loss function is `categorical_crossentropy`, which requires one-hot-encoded labels, eg. [1,0,0] for cat, [0,1,0] for dog and [0,0,1] for snake.
It is also important to mention that there is also the `sparse_categorical_crossentropy`loss function, which does exactly the same but requires the labels to be integer, which is not the case in the current codebase. Initially, we were unaware of the difference and accidentally used the wrong `sparse_categorical_crossentropy` loss function, which prevented the code from running and resulted in a long error message. This problem occurred due to a misconception that there would be only one categorical crossentropy loss. We ignored the "sparse" prefix in the beginning and only looked it up later when the error message appeared.  
There are also plenty of other loss functions in the realm of data science and neural networks, such as Kullback-Leibler Divergence, common for variational autoencoders (VAEs) to measure the difference between the approximate posterior distribution and the true prior distribution or the hinge loss in conjunction with SVM. 
In our case, `categorical_crossentropy` is the most common choice for multiclassification neural networks. Neural networks that only distinguish between two classes would use `binary cross-entropy` loss, which can be regarded as a simpler form of `categorical_crossentropy` loss.

### 2.3 CNN Architectures
As already mentioned, three different CNN architecture types were tested in this milestone. The main difference between these architectures lies in their size.
Starting with the smallest CNN architecture, which only has 2 convolutional layers and one fully connected layer at the end. The subsequent medium CNN has one convolutional layer more and two fully connected layers at the end instead of only one. In the end, the large CNN consists of four convolutional layers and two fully connected layers to avoid unnecessary complexity. 
Thus, each new model scales up in complexity by deeper layers, higher filter counts and additional fully connected layers to capture the patterns in the Data. However, the larger the network, the more important regularization, becomes to avoid overfitting to the training data and generalising poorly on new, unseen data. 
This is achieved by dropout, which removes a certain portion of the neuron connections while training, making the network less dependent on single neurons.
The defined kernel sizes and pooling sizes are chosen by good feel and common CNN architecture definitions because the task did not ask to find the optimal hyperparameters because this action is very time-consuming and resource-intensive.
Hence, it was just tried out how different network sizes affect the final model performance.  
For the final project, it seems to be important to define more models and do this analysis more systematically. All information about all hyperparameters can be found in this [online book](https://d2l.ai/chapter_convolutional-neural-networks/index.html).

### 2.4 Model Evaluation
The selected evaluation metric, which we have choosen is accuracy. The reason for this is that we have at the moment a balanced dataset with a equal number of cat, dog and snake images.  
Moreover the false postive or flase negative are equally bad, because both types of errors result in misclassification of animals, which defeats the main purpose of our model of predicting all anaimal types correctly.  
For instance, a false positive where a dog is classified as a cat, or a false negative where a snake is classified as not a snake, carries the same affect for us in terms of model performance degradation.  
Thus, the use of accuracy as the evaluation metric aims to measure the overall effectiveness of the model in correctly identifying each class without introducing bias toward any particular category.

## Task 3 - Data analysis in Jupyter Notebook 
First we needed to check if Jupyter Notebook was installed in our VS code. We used `jupyter notebook --version` and 
got `7.3.1` as answer. Then we could start making the exercises.

### Loading data from Numpy Array with dimensions where channels is 3 in an RGB image
The dataset analysis began with loading image data into Numpy arrays. A Python function was implemented to download 
images from given URLs using the requests library and the PIL module. The downloaded images were then converted 
into Numpy arrays. Each Numpy array had the shape (width, height, channels), with the channels dimension equal to 
3, representing the RGB color channels (Red, Green, and Blue).
The images were organized into three classes: dogs, cats, and snakes. For each class, the number of images and the 
shape of the first image were printed to confirm successful loading. This step ensures the dataset structure is 
intact and provides preliminary insights into the image dimensions.

### Analyze data with Numpy
Basic statistics about the dataset were calculated, such as the number of images per class and their dimensions. 
The uniformity of image dimensions across the dataset was verified to ensure compatibility with subsequent analysis.
To get a visual understanding of the dataset, a 3x3 grid of random images from each class was displayed using 
Matplotlib. This allowed an intuitive inspection of image quality and content, helping to confirm that the data was 
loaded correctly.
For each class, histograms of pixel intensities were created for the Red, Green, and Blue channels. This analysis 
revealed differences in color distributions between the classes, offering a basis for distinguishing them.
The RGB images were converted to the HSL (Hue, Saturation, Lightness) color space using the PIL library. Histograms 
for the Hue, Saturation, and Lightness channels were plotted. The HSL analysis provided an alternative perspective 
on color characteristics, aiding in understanding class-specific features.
To explore patterns and relationships in the dataset, dimensionality reduction was applied using PCA (Principal 
Component Analysis). Each image was flattened into a 1D array, and the PCA algorithm reduced the dataset to two 
dimensions. A scatter plot was created to visualize the classes in 2D space, revealing clusters and overlaps 
between the classes. This step helped uncover separability and shared characteristics across the dataset.



