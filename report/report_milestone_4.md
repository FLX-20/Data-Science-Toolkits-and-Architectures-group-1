# Milestone 4

## [Task 1](https://github.com/FLX-20/Data-Science-Toolkits-and-Architectures-group-1/issues/43) - Evaluation Metrics and Weights and Biases
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





## [Task 2](https://github.com/FLX-20/Data-Science-Toolkits-and-Architectures-group-1/issues/45) - Improving Model Performance

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

#### 2.5 Weights and Biases Dashboard
On the [weights and biases dashboard](https://wandb.ai/fe-pappe-dsta-1/cnn-training/workspace?nw=nwuserfepappe) it is clearly visible that all three models almost reach the same accuracy of around 0.70 after 20 epochs.
This can be a first indication that the dataset could be too small and not diverse enough to predict the correct label with high accuracy.
However, it is too early to draw a final conclusion, because only three models have been created and a detailed model selection has not been conducted.
According to Occam's razor, we would select the smallest CNN for which the confusion matrix is created in the end.

## [Task 3](https://github.com/FLX-20/Data-Science-Toolkits-and-Architectures-group-1/issues/45) - Data analysis in Jupyter Notebook 
Thanks to the Jupyter Notebook extension in VS Code, `.ipynb` files can be easily created and modified.
Furthermore, (Jupyter)[https://pypi.org/project/notebook/] and (IPython)[https://pypi.org/project/ipykernel/] have to be installed installed in the current Python environment. This can be done with the following command.
```
pip install notebook ipykernel
```
This allows us to run `.ipynb` files in the VS-Code working environment. The created notebook includes the functionalities for loading the data, showing a random sample of images from each class, creating the rgb-histograms and hsv-histograms for each each class. These steps are closer explained in the next chapters.

### 3.1 Downloading the Data
In the first step, the dataset is downloaded from Kaggle in the same way as in our actual project codebase.
The main difference is that the exception handling was removed, which is not necessary in a Jupiter notebook because the code blocks are executed sequentially and manually by the user. Thus this exception handling only adds additional overhead here from our point of view.
The final downloaded images were organized into three classes: dogs, cats, and snakes.

### 3.2 Loading Data into Numpy Array
In the next step, the images of each class are loaded into a separate numpy arrays. Each Numpy array has the shape (num_class_img, width, height, channels), with the channels dimension equal to 3, representing the RGB color channels (Red, Green, and Blue), and num_class_imag equal to 1000 because each class consists of 1000 images.  
All images in the dataset have a height and a width of 256 pixels. In our main project codebase, the images are scaled down to 128 pixels, because of the limited computation capacities of our computers. However, in this analysis, we will continue with the original image size.

### 3.3 Showing Images of each Dataset
In the subsequent part of the data/image analysis, random images of each class are shown in a 4 by 4 grid to get a first impression of the data.
There is no random seed in this code, meaning every time the code is executed new random 16 images of each class are shown. 

### 3.4 RGB-Histogram
The RGB histograms for each class were generated by counting the occurrences of each colour value. 
To simplify the analysis, we chose a bin size of 32 instead of using all 256 individual values. 
This means that consecutive values are grouped into a single bin; for example, values ranging from 0 to 31 are combined into one bin instead of being represented as 32 separate bins.  
Furthermore, the y-axis was changed from absolute values to relative frequency, describing the proportion of pixel occurrences 
within each bin relative to the total number of pixels in the image or class. This makes interpretation easier and the y-axis is independent of the number of images loaded.  
The visualization of the histograms of the three classes shows some small differences in the colours of the images.
The red and green channels of the cat histogram appear uniform except at the end where you can see a decrease starting around 180. 
But both histograms peak in the end at high pixel values. The blue channel histogram on the other side shows a gradual decline from low values to high values, 
but also with a smaller peak at the end. Thus shows a balanced RGB spread but with brighter peaks compared to the other classes.  
Also, the dog's histograms show a form of uniform distribution, but in a weaker form due to the higher counts in the middle.
Altogether this indicates smooth and even colour-balanced images.
On the other side, the RGB histograms for the snakes show stronger colour contrasts, 
because of the large peaks in the dark and bright regions of all channels. These peaks can be seen in all histograms but in the snakes once it is the most intense form.


### 3.5 HSV-Histrogram
In the last step the HSV-Histograms are created. HSV-colours represetns colors using Hue (H), Saturation (S) and Value(V),
like shown on the next image.  
![A descriptive alt text](https://upload.wikimedia.org/wikipedia/commons/3/33/HSV_color_solid_cylinder_saturation_gray.png)  
The **Hue** represents the type of colour in form of defrees from 0 to 360. The most important degrees are: 0° (red), 60° (yellow), 120° (green), 180° (cyan), 180° (blue) and 300° (Magenta).
If you rotate the wheel once, you transtion smoothly through the rainbow spectrum.
The **Saturation** states how intense the colour is, ranging from 0% to 100% or 0 to 1.
0% means completely desaturated (graysacle). On the other side 100% is fully saturated.
The last channel is the **Value**, which refers to the brightness of the colour. It also ranges from 0% to 100% or 0 to 1.
Here 0% is black, meaning no brightness and 100% is full brightness. 

So, the RGB values were converted into HSV values, and the three new colour channels were represented again in histograms.
From the cats' histograms, it can be concluded that cat images predominantly have warm hues (red, orange, and yellow) because of the higher concentration of hue between 0° and 50°.
Moreover, a low saturation and a balanced lightness distribution can be seen in the other two cat histograms.
The dogs' histogram exhibits slightly broader hues compared to the cat histogram.
Moreover, the saturation can be described as muted, and the lightness is again well-distributed.
All this emphasizes a diverse but still natural colour palette for dogs.
The snakes' histogram reflects again the colourful but also highly contrasted nature of snake images, due to the high peaks in all plots.

### Final conlsusion of analysis
Both the RGB and HSV show different distributions for cats, dogs, and snake images.
However, it can be noticed that the cat and dog images are more similar regarding their color compared to the snake images. This might be one reason why our CNN more often misclassifies cats as dogs or dogs as cats than it does with snakes. This can be seen in the confusion matrix of all the neural networks.



