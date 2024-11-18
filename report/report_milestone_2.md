# Milestone 2

## 1 Establishing a Clean Git Repository



## 2 Technical Concepts and Tool Preferences



## 3 Building Core Functionality for Model Training and Prediction



## 4 Code Modularization and Structure Enhancement

### 4.1 Adjusting Codebase Strcuture
The new codebase after running the `download_datasets.sh` is structured in the following way. 
```
DATA-SCIENCE-TOOLKITS-AND-ARCHITECTURES-GROUP-1
│
├── datasets/
├── images/
├── models/
├── report/
├── scripts/
├── src/
│   ├── __pycache__/
│   ├── data_loader.py
│   ├── evaluate.py
│   ├── main.py
│   ├── models.py
│   ├── save_load_models.py
│   ├── train.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
```
All python module are stored in the `src` folder. This folder includes:
1) In the `main.py` module the parser is implemented, which calls the required function based on its inputs for training, testing or classification.
2) In the `models.py` module the structure of the model is defined. So far, there is only one CNN model in this module. This design decision should make future developments easier because several CNN models with the number of layers and kernel shapes can be defined here. Afterwards, these different models can be compared to each other based on the previously selected metrics in the `evaluation.py` module.
3) In the `evaluation.py` module there are all functions for testing and evaluating the model, such as the function for the calculation of the model accuracy and loss based on the test datasets and the function to draw the confusion matrices. Furthermore, the classification function for single images is also included in this module. This function can be considered as a kind of human evaluation because for simple scenarios we humans can quite well differentiate cats, dogs and snakes or another classification task. But in most cases, the computer is faster.
4) In the `save_load_models.py` the saving and loading of trained models is implemented. In the past, the function was split into different modules. But this splitting seemed to be too small. 
5) In the `data_loader.py` module the data is loaded from the local directory and preprocessed for the CNN. 
5) In the `train.py` module the train process takes place. So far it only includes the the train function, which is quite less for one module. But for future development and extending this function more easily, it was also separated into an additional module.

Moreover addtional directories are create for shell-scripts (`scripts`), for images that are created by the code (`images`) and for datasets for model training and testing (`datasets`)
In the root directory there are the `.gitignore`,`README.md` and `requirements.txt` files, like in the previous milestone. The only new file here is the `dockerignore` file to exclude directories and files from teh docker build process.

Overall, the codebase is separate and very detailed. This detailed structure was chosen to be prepared to be prepared for future milestones because we don't know yet how complex and complicated the code will become in the next weeks.
This is why it seemed better to have a more detailed codebase structure.






## 5 Dependency Management with pip and Virtual Environments



## 6 Containerizing the Application with Docker