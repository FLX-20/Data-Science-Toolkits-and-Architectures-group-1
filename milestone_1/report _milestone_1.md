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

## 5. Explaining Convolutional Neural Networks

## 6. Adding Documentation
The README.md, which is always shown on the first page of the repo, was extended with all important information to run the code of the first milestone. Afterwards, we deleted the repo from our machine and tried to set up a local copy of the repo on our machines following the steps in the documentation. 

## 7. Creating a folder for this milestone

