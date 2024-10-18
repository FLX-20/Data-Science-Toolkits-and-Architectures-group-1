# Data Science Toolkits and Architectures - *Milestone 1*


## 0. Setting up a virtual Machine with Ubuntu

## 1. MNIST-Dataset

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

## 7. Creating a folder for this milestone

