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






## Task 3 - Data analysis in Jupyter Notebook 





