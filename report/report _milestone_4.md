# Milestone 4

## Task 1 - Evaluation Metrics and Weights and Biases
First we all made an account at Weights and Biases [website] (https://www.wandb.com/).
Afterwards we completed the tutorial on [GoogleColab] (https://colab.research.google.com/drive/1pMcNYctQpRoBKD5Z0iXeFWQD8hIDgzCV)

### 1.1 Experiment Management and its importance
Experiment management is all about keeping track of everything you try while building machine learning models - 
things like the data you use, the model settings, the code version, and how well each experiment is performed.
The importance of experiment management is to make it easier to reproduce results, save time, helping teammates
to make clear what is been done, and it lets you analyze what worked and what did not.

### 1.2 Metric in ML
In ML, a metric is just a way to measure how well your model is doing. For example
if you work on classification, you might look at metrics like accuracy or precision.
If you are predicint numbers, you might use something like mean squared errors.
Metrics are super important because they tell you if your model is actually solving the problem or not.

### 1.3 Precision and Recall, the trade-off between the two
Precision is about how many times your positive predictions are correct. 
For example, if your model says that 10 emails are spam while actually 8 of them are spam, 
then you have a 80% precision.
Recall is about how many of the actual positive cases your model found. If there were
20 spam emails and your model only flagged 8, your recall is 40%.
The trade-off between the two terms happens often because focusing on one can hurt the other.
If you only mark emails as spam you are 100% sure that you miss a lot of spam. On the other hand, 
if you try to catch all the spam, you might flag some valid emails by mistake.
The right to balance depends on what is more important in your situation.
For example, in detecting diseases, recall is more important because you do not want to miss any cases.
But in spam detection, precision matter more, therefore you do not mark any important emails as spam.

### 1.4 AUROC Metric
AUROC stands for Area Under the Receiver Operating Characteristic Curve.
It is basically a way to measure how good your model is at distinguishing between two classes, for example spam or no spam.
The ROC (Receiver Operating Characteristic Curve) itself shows how well the model balances true positives
and false positives at different thresholds. The AUROC is just the area under that curve. A perfect model gets an AUROC of 1. 
A useless model gets 0.5, which in other words mean that you also could guess.
The AUROC metric is great because it works no matter what threshold you pick and gives you a single score to compare models.


### 1.5 Confusion Matrix
A confusion matrix is a table that breaks down how well your model did in a classification problem. The table shows
True Positives (TP), True Negatives (TN), False Postives (FP), and False Negatives (FN)
TP is when the model correctly predicts something postive. TN is when the model correctly predicts something as negative. 
FP is when the model says something is positive, while it is not. FN is when the model misses a positive case. 
The confusion matrix is useful because it lets you calculate all sorts of metrics like precision, recall, accuracy,
and gives you a clearer picture of where your model is messing up. 
Therefore, the confusion matrix can be used to measure precision and recall.
Precision is calculated through: 
\[
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
\]
This shows how often the model's positive predictions are correct.
Recall can be calculated through: 
\[
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
\]
This shows how many actual positives the model manages to find.





## Task 2 - Improving Model Performance

After a `Weights and Biases` account had been created, the existing codebase was instrumented with `Weights and Biases` features.  This was achieved by adding a new operational mode, besides, `download_data`, `train`, `test` and `all`. This mode is `wandb_run`, which builds several models defined in a JSON file and transmits the results to the Weights and Biases server. In this way, one can evaluate the models in the related web-application.

## 2.1 Login to W&B
The API key is used to log in to `W&B`. This key is saved in the `.env` file, which is stored only locally on the host machine and is not shared on the remote GitHub repo. Hence, if you want to run the code, you have to enter your own `W&B` key to access the results in the web application.  
The API-key is added as a environment varaible of the docker container by adding it to the `environment` section of the docker-compose file. Docker-compose reads in automattically all required variables form the `.env`-file and adds them as environement variables in the `app` container.

## 2.2 Model Training
Before the model can be trained the CNN architecture has to be loaded from the regarding JSON file.  
This code architecture, incorporating the reading from a JSON, was chosen to run several CNN model tests in a sequence. Because the code is not hard coded, it will be easier in the future to try out different hyperparameter combinations of CNNs, making it easier to find an appropriate model.  
Before the model can be trained the cnn arichtecture have to be loaded from the regarding json file.
This code architcture incoperating the reading from a json-file was choosen to run several cnn models test in a sequence, which will make it easier in the future to try out different hyperparameter combinations, because the code is not hard coded.
After the model was build with the `build_model_wandb` function it is trained in the subseqent step.
Normally one wourd you the [Adam](https://arxiv.org/abs/1412.6980) (Adaptive Momentum Estimation) optimizer for updating the weights in the neural network. But Stochastic Gradient Descent was also added as an option. However, it is not assumed that SGD adds better results, because Adam-optimized is an improved version of SGD, which also combines momentum optimization and RMSP (Root Mean Squared Propagation) to achieve better convergence. Momentum helps accelerate gradients in the right direction by averaging past gradients, while RMSProp adjusts the learning rate for each parameter based on a running average of recent gradient magnitudes, preventing oscillations.  
Nowadays, the Adam optimizer is used in most of the papers, because it achieves so far the best results in many situations. From my own experience, it can be said, that the optimizer does seem to have a tremendous influence. Larger performance boosts can be achieved with other hyperparameters. 
The used loss function is `sparse_categorical_crossentropy`, which requires the true labels be represented as integer values rather than one-hot encoded. 
It is also important to mention that there is also the `categorical_crossentropy` loss function, which does exactly the same but requires the labels to be one-hot-encode, which is not the case in the current codebase. In the beginning, we didn't know the difference and accidentally used the wrong `categorical_crossentropy` loss function. The mistake was noticed quite late because the code still runs. But due to the wrong encode the accuracy does not increase no matter how hard you try to change the hyperparameters.  
There are also plenty of other loss functions in the realm of data science and neural networks, such as Kullback-Leibler Divergence, common for variational autoencoders (VAEs) to measure the difference between the approximate posterior distribution and the true prior distribution or the hinge loss in conjunction with SVM. 
In our case, `categorical_crossentropy` is the most common choice for multiclassification neural networks. Neural networks that only distinguish between two classes would use `binary cross-entropy` loss, which can be regarded as a simpler form of `categorical_crossentropy` loss.

## 2.3 CNN Architectures
As already mentioned, three different CNN architecture types were tested in this milestone. The main difference between these architectures lies in their size.
Starting with the smallest CNN architecture, which only has 2 convolutional layers and one fully connected layer at the end. The subsequent medium CNN has one convolutional layer more and two fully connected layers at the end instead of only one. In the end, the large CNN consists of four convolutional layers and two fully connected layers to avoid unnecessary complexity. 
Thus, each new model scales up in complexity by deeper layers, higher filter counts and additional fully connected layers to capture the patterns in the Data. However, the larger the network, the more important regularization, becomes to avoid overfitting to the training data and generalising poorly on new, unseen data. 
This is achieved by dropout, which removes a certain portion of the neuron connections while training, making the network less dependent on single neurons.
The defined kernel sizes and pooling sizes are chosen by good feel and common CNN architecture definitions because the task did not ask to find the optimal hyperparameters because this action is very time-consuming and resource-intensive.
Hence, it was just tried out how different network sizes affect the final model performance.  
For the final project, it seems to be important to define more models and do this analysis more systematically. All information about all hyperparameters can be found in this [online book](https://d2l.ai/chapter_convolutional-neural-networks/index.html).

## 2.4 Model Evaluation
The selected evaluation metric, which we have choosen is accuracy. The reason for this is that we have at the moment a balanced dataset with a equal number of cat, dog and snake images.  
Moreover the false postive or flase negative are equally bad, because both types of errors result in misclassification of animals, which defeats the main purpose of our model of predicting all anaimal types correctly.  
For instance, a false positive where a dog is classified as a cat, or a false negative where a snake is classified as not a snake, carries the same affect for us in terms of model performance degradation.  
Thus, the use of accuracy as the evaluation metric aims to measure the overall effectiveness of the model in correctly identifying each class without introducing bias toward any particular category.

## Task 3 - Data analysis in Jupyter Notebook 





