# Milestone 2

## 1 Establishing a Clean Git Repository

### 1.1 New Git structure and related issues
In the first step of this second milestone, we thought about a better structure for our git repo.
The result was that the report was divided into two large parts. 

- `main-report-branch` for finished report chapters 
- `main-dev-branch` for finished code features

Thus, for every new feature in the code, a new branch was created and merged after its completion into the `main-dev-branch`.
The same idea was applied to the `main-report-branch` based on chapters.
At the end of the project, the final results of the `main-dev-branch` and `main-report-branch` were merged into the `main branch.`
Furthermore, we added a rule that a pull request and a review by a second person from the team are also necessary for the `main-dev-branch` and `main-report-branch`.

This idea worked fine until we encountered our first merge conflict. Github informed us that we needed to resolve this conflict locally on our machine by using the following commands.

```shell
git pull origin main-dev-branch # step 1
git checkout save-model #step 2
git merge main-dev-branch #step 4
# step 4) Fix the conflict
git push -u origin save-model # step 5
```
However after successfully fixing the merge conflicts, we were not able to push the results to the `main-dev-branch` of our GitHub repo anymore, 
due to the rule that no merge is allowed without a pull request. 
We solved this problem by switching this rule for all branches except the `main` branch. But we are aware that this might not be the most professional solution.
So your question for the next time would be:   
**How can we create a rule for the branches `main-report-branch` and `main-report-branch` that requires a pull request for all merges into these branches, but still can resolve merge conflicts?**

### 1.2 Gitignore File
A `.gitignore` file was already created in the last milestone together with the creation of the git repository.
In the beginning, we used the default git `.gitignore`-file provided by GitHub. This file was extended to also exclude the `datasets`, `models` and `images` libraries because we want to upload neither the large training dataset to GitHub nor our trained models, which were created during the development to test the code.   
However, we would like to make the datasets, which we used for this code quickly available for other users. This is the way we created the `download_datasets.sh` script, which automatically creates the required directories and downloads the two datasets.

### 1.3 Sharing the .gitignorefile
The .gitignore file was continuously updated when a new feature was merged into the `main-dev-branch`. However, this did not happen frequently because the default GitHub version was already quite complete for this milestone. We only added the following directories to avoid uploading images and datasets to the repo.
```
datasets/
models/
images/
```
An extra .gitignore strategy for these three extra lines would have caused more work than benefit. But we are trying to continuously improve our git branching strategy over all milestones and adapt it if there is a necessity and the tasks become too complex to solve with our simple strategy.