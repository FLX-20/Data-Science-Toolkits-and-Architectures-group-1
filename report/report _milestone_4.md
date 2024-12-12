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



## Task 3 - Data analysis in Jupyter Notebook 





