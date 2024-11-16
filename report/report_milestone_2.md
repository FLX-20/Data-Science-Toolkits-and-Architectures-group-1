# Milestone 2

## 1 Establishing a Clean Git Repository

# 1.1 New Git structure and related issues
# 1.1 New Git structure and related issues
In the first step of this second milestone, we thought about a better structure for our git repo.
The result was that the report was divided into large parts. The `main-report-branch` is for finished report chapters 
and the `main-dev-branch` is for finished code features.
Thus, for every new feature in the code a new branch was create and merged after its complition into the `main-dev-branch`.
The same idea was applied to the `main-report-branch` based on chapters.
At the end of the project the final results of `main-dev-branch` and  `main-report-branch` were merged into the `main`branch.
Furthermore we added a rule that also for the `main-dev-branch` and `main-report-branch` a pull-request and a review of a second person form the team is necessary.

This idea worked fine until we ran into our first merge conflict. Github informed us that we have to resolve this conflict localy on our machine by the following commands.

```shell
git pull origin main-dev-branch # step 1
git checkout save-model #step 2
git merge main-dev-branch #step 4
# step 4) Fix the conflict
git push -u origin save-model # step 5
```
However after successfully fixing the merge conflicts, we were not able to push the results to our GitHub repo anymore, 
due to the rule that no merge is allowed without a pull request. 
We solved this problem by shortly switching of this rule. But we are aware that this might not be the most professional solution.
So our question would how to deal with such an issue the next time? How should we deal with an merge conflict in an pull-request, which we should resolve localy but can not push to the github repo in the end, because of our strict merging rules?

## 2 Technical Concepts and Tool Preferences



## 3 Building Core Functionality for Model Training and Prediction



## 4 Code Modularization and Structure Enhancement



## 5 Dependency Management with pip and Virtual Environments



## 6 Containerizing the Application with Docker