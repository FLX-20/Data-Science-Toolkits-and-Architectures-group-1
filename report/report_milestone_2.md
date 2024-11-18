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

## 2. General Questions 

### 2.1 Hash-Functions

A hash function is a mathematical process that transforms an input, typically a message or piece of data, into a fixed-size string of characters, often represented as a series of bytes. This output, called a hash value or digest, acts as a unique 'fingerprint' of the original input. A key feature of a good hash function is that even a small change in the input will produce a completely different hash value. 
One of the most popular hash functions is SHA-1, which stands for "Secure Hash Function".

One of the main requirements for hash functions is collision resistance, meaning that it should be highly unlikely, or basically impossible, for two different inputs to produce the same output. If this happens, it's called a collision and indicates that the hash function may not be secure or suitable for certain applications.

Hash functions are essential for password storage and verifying data integrity, for example: Instead of storing passwords in clear text, systems often store only the hash of the password. Even if a malicious actor were to gain access to the database, they would only see the hash values, not the original passwords, making it much harder to compromise user accounts. As for Data Integrity, the most ubiquitous application which all of us know is probably WhatsApp, here the “SHA-256” is used in order to verify that messages have not been tempered with between the sender and the receiver.
Hash values and functions are therefore also used when downloading files from official repositories, such as docker, to ensure that the data has been transferred completely unchanged. 
This is done by the server generating a hash value and sending it together with the desired package from the client. The client receives the packet and the hash value and also calculates the hash value using the same hash function. If the transfer was successful, the two hash values must match.


### 2.2 Python modules, packages and scripts:

**Python module:** A module is a single Python file (with a .py extension) containing Python code. Modules are used to organise and reuse code, in other words they act as building blocks. 

**Python package:** A package is a collection of modules organised in directories. A directory containing a __init__.py file (even if it's empty) is recognised by Python as a package. Packages allow Python code to be structured hierarchically, making it easier to manage and keep track of large code bases.

**Python script:** A script is a Python file designed to run as a standalone program. Unlike modules and packages, which are designed to be imported, scripts are designed to perform a task, such as running a program or automating something when executed.

In summary, a module is a single file, a package is a directory containing multiple modules, and a script is a file designed to run directly.

### 2.3 Docker Containers and Volumes (ELI5).  [chroot = root directory]

A **Docker container** is like a TV dinner. It comes packaged with everything you need to make a specific meal, right in the box. When you’re done, you can throw it away. No matter where or how you heat it up (microwave, oven, or stovetop), it’s going to taste the same every time, anywhere you “use” it.  
 
A **Docker volume** is like the fridge or freezer where you store your TV dinners. The fridge stays there even if you take out a meal, and you can put things back in to save them for later. Even if you get rid of the container (TV dinner) after eating it, the fridge (volume) will still be there, holding other meals or leftovers, keeping things safe and unchanged for next time.

### 2.4 Python Virtuale and Docker, Use cases:

Both Python virtual environments (virtualenv) and Docker are tools that help create isolated environments, but they are suited to different use cases.

**Python Virtualenv:** As the name suggests, Python Virtualenv(ironment) is ideal for setting up a lightweight, Python-specific environment on a machine where the project dependencies are all Python packages. It separates the system Python environment from the project Python environment to avoid version conflicts between the required package versions of the project and the current operating system, due to its isolated Python dependencies for the specific project.
They are used for small medium projects, where only Python libraries and their dependencies need to be managed. It should be used as a lightweight option to develop and test Python code locally without concerns about the broader system environment.
As soon as you want to work with other people, which use different operating systems it might make sense to use docker to avoid problems caused by the characteristics of the operating system. 

**Docker:** on the other side creates isolated environments for the entire application. It is recommended to use Docker if the project has system-level dependencies or needs a fully isolated environment that includes the OS, specific versions of system libraries, or non-Python dependencies (e.g. a database, a specific version of Python etc.). Docker is also more portable because the container can be shared across (operating) systems and machines while ensuring consistent behaviour.

To sum up: For pure Python projects on your personal local machine, virtualenv is often simpler and faster, while Docker is preferable for complex, multi-language applications,  the exact same environment needs to be replicated across different machines or a group of developers with different machines wants to work together with less troubleshooting why the code is only running on one machine, like in this project.

### 2.5 What is the Docker build context?

The Docker build context is the set of files and directories the Docker daemon has access to when you run Docker Build. 
```shell
docker build -t my-image .
```
In the case of MacOS or Windows users, it is "Boot2docker", which spins up a Linux virtual environment. It defines what Docker can see while building the image. Typically, it's the directory where the Docker file is located, so everything in that directory is included in the build context and accessible to Docker during the build process.  
The build context can affect build performance. For example, if your project directory contains a lot of files that aren't needed to build the Docker image, this can slow down the build process. Therefore, it's a good practice to include only necessary files and use `.dockerignore` to exclude unnecessary files.


### 2.6 How Can You Assess the Quality of a Python Package on PyPI?

To assess the quality of a Python package on PyPI (Python Package Index), one should consider the following factors.

1) The number of downloads is a key indicator of quality. The fact is that popular packages with high download counts are more reliable. It's simple: more people use and test them.
2) The number of stars and contributions on GitHub are also useful indicators. Many PyPI packages are hosted on GitHub. A package with a high star count, active issue discussions and frequent updates is a good indication of quality.
3) Furthermore, Documentation is essential. Good packages are most likely to come with comprehensive documentation, including usage examples, installation instructions, and explanations for each feature. Packages with thorough documentation are more reliable and accessible, making them easier to use.
4) Code quality and tests are also important factors to consider. If you can access the package's source code, you should be able to check for the presence of tests (e.g. a /tests directory). The tests prove that the developers guarantee the reliability and functionality of the code.
5) You should be able to see a version history and recent updates. If a package is frequently updated, it is almost certainly well-maintained. Checking the version history shows you how active the development is and how responsive the maintainers are to issues.
6) You should also check for dependencies. Some packages depend on many other libraries, which undoubtedly makes their usage more complex and introduces vulnerabilities or conflicts(dependency hell). Fewer dependencies mean easier integration.
7) Lastly, User feedback can be a worthwhile source or rather indicator of qualitatively good Python Packages. Reading reviews or issues posted in GitHub repositories can thus allow one to form a better opinion, as the community will highlight any recurring problems or concerns with the package.

In conclusion, assess a Python package by looking at its popularity, maintainability, community feedback, and overall code quality. These factors mentioned above provide a well-rounded overview of their respective qualities. 


## 3 Building Core Functionality for Model Training and Prediction
## 3.1 Load Datasets
The starting point of loading new datasets for training the model was the [tensorflow documentation for dataloading](https://www.tensorflow.org/tutorials/load_data/images).
The objective was to implement a function that can read datasets from the local filesystem and return the same values as the data loading function for the already included datasets in TensorFlow, such as mnist_fashion or cifrar10. These datasets can be easily loaded with the following functions.
```python
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
```
This objective was defined on our own because the task included too little information. Questions about the data format, the kind of data or the data structure were not clarified. This is why we defined them on our own. 
The dataset has to be already extracted (e.g. unzip) and has to be placed in the `datasets` directory. Inside the directory of each dataset, there has to be a subfolder with the images for every class. 
The Directory structure for the two datasets, which were used to test the code, is presented in the next code block.
```
DATA-SCIENCE-TOOLKITS-AND-ARCHITECTURES-GROUP-1/
├── datasets/
│   ├── Animals/
│   │   ├── cats/
│   │   ├── dogs/
│   │   └── snakes/
│   └── flower_photos/
│       ├── daisy/
│       ├── dandelion/
│       ├── roses/
│       ├── sunflowers/
│       └── tulips/
└── LICENSE.txt
```
These datasets can be installed by executing `download_datasets.sh`. 
In the beginning, downloading the datasets was included in the Python code. However, if you run the code multiple times it is redundant and causes unnecessary computation to download the datasets every time again.
This issue resulted in the decision to exclude this step into a shell script. 

## 3.2 Training the Neural Network
The Convolutional Neural Network can be trained by executing the following command after building the docker image.
```
docker run --rm \
 -v ./images:/app/images \
 -v ./datasets:/app/datasets \
 -v ./models:/app/models simple_cnn \
 --mode train \
 --dataset_path /app/datasets/Animals \
 --model_file_path /app/models/cnn_model.keras \
 --batch_size 64 \
 --epochs 20
```
This version of the code uses a parser to modify some of the inputs such as the `dataset_path`, `model_file_path`, `batch_size` and `epochs` via the CLI, instead of storing them in an additional config file. This makes it possible to run the code quickly with different datasets or batch sizes.    
The actual structure of the CNN and the related training process was not changed in this milestone, because we assume that this is part of the next milestone. 
Thus, the final model accuracy and the confusion matrix for both datasets are not optimal and much space for further improvement. 

## 3.3 Saving the Model
After the model training the model is saved as a `.h5` or `.keras` file in the model's directory, which is created by the download_datasets.sh script. The decision to provide both file types came from the note in the documentation that the `.h5` filetype is deprecated and the newer version `.keras` is recommended.  
If the file ending provided via the parser is neither `.h5` nor `.keras` an error message is printed out.  
It is also important to mention that we are aware that not all edge cases for inputs via the parser are modelled out. This could be improved in the future by better exception handling to improve the stability and robustness of the code. 
As long as this is not the case the code should be exactly executed how it is described in the `README.md`.

## 3.4 Loading files and Model Evaluation
The trained stored model can be loaded afterwards by using this command in the CLI.
```
docker run --rm \
 -v ./images:/app/images \
 -v ./datasets:/app/datasets \
 -v ./models:/app/models simple_cnn \
 --mode test \
 --dataset_path /app/datasets/Animals \
 --model_file_path /app/models/cnn_model.keras \
```
The important thing here is the change of the `--mode` form `train` to `test`. Without training a model and saving this function will result in an error. 
If the command is executed the model and the related dataset are loaded. But this time we are only using the test data for model evaluation. The model evaluation only consists of the loss and accuracy, like in the previous milestone.  
The a new added function in the evaluation part is the confusion matrix, which is stored in the `image` directory, like 9 example images from the test and train part of the dataset. 

## 3.5 Performing predictions with the trained model
The last `--mode` of the parse in this project is `classify`, which allows to make a prediction using a trained model from a local image which is stored in the `datasets` or `ìmages` folder and provided to the code via the CLI as parser argument. 
```
docker run --rm \
 -v ./images:/app/images \
 -v ./datasets:/app/datasets \
 -v ./models:/app/models simple_cnn \
 --mode classify \
 --single_image_path datasets/Animals/dogs/your_image_name.jpg
```
This allows classifying any image from the internet. The example of the code above. The image is classified as a cat, dog or snake. 

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

Moreover, additional directories are created for shell-scripts (`scripts`), for images that are created by the code (`images`) and for datasets for model training and testing (`datasets`)
In the root directory, there are the `.gitignore`,`README.md` and `requirements.txt` files, like in the previous milestone. The only new file here is the `dockerignore` file to exclude directories and files from the docker build process.

Overall, the codebase is separate and very detailed. This detailed structure was chosen to be prepared to be prepared for future milestones because we don't know yet how complex and complicated the code will become in the next weeks.
This is why it seemed better to have a more detailed codebase structure.

### 4.2 Formatting Code according Pep8

“Pep8” is the acronym for “Python Enhancement Proposal 8”.
This proposal contains guidelines and conventions on how to write (python) code that is more standardized and thus allows for easier readability, which in turn fosters understanding and makes collaboration (and documentation) more streamlined and accessible.
Exemplary conventions include utilizing 4 indentations instead of tabulating, limiting code lines to 79 and documentation lines to 72 characters respectively and only ever importing one module per line of code.  
Formatting code according to Pep8 can be quite hard and tedious. This is the way the autopep8 extension was installed in vscode. After the installation of this extension and modification of the JSON settings file with the following lines code is auto-formated according to pep8 evertime, when it is saved.
```json
  "[python]": {
    "editor.defaultFormatter": "ms-python.autopep8",
    "editor.formatOnSave": true
  }
```

## 5 Dependency Management with pip and Virtual Environments

### 5.1 Traditional Virtual Environment and Dependency Management
In Python, virtual environments are necessary to separate project-required dependencies from system-wide packages. This avoids conflicts between packages. 
A virtual environment can be created and activated with the following commands.
```shell
python -m venv venv
source venv/bin/activate
```
You can check if `venv` was successfully created with `which pip`. 
After the change of the environment, all newly installed packages are stored in this `venv`. 
The simplest way to create a `requirements.txt` is to use `pip freeze` to list all installed packages and their version and pip them into the `requirements.txt` file.
```shell
pip freeze > requirements.txt
```
After the creation of this file, it can be used by other people to quickly install all required packages at once in their virtual environment to run the code.
```shell
pip install -r requirements.txt
```

### 5.2 Advanced dependency Management with pip-tools
A more sophisticated way to manage dependencies is `pip-tools`, which allows to separate between direct dependencies and transitive dependencies.
- direct dependencies: packages directly required by the project
- transitive dependencies: packages required by the projects' packages.
 
The package `pip-tools` can be installed, like any other package with pip in the following way.
```shell
pip install pip-tools
```
After the installation of `pip-tools` and the creation of a `venv`, like in the previous chapter, a `requirements.in` file can be created.
```
tensorflow
numpy
matplotlib
scikit-learn
keras
```
This file only lists the direct dependencies of our project.
In the next step `pip-tools` use this `requirements.in` to generate the `requirements.txt` with the following command. 
```shell
pip-compile requirements.in
```
The final `requirements.txt` can then be used like in the previous chapter.

## 6 Containerizing the Application with Docker
Docker is an open-source platform for building, testing and deploying applications quickly. It packages software into standardized units, which are called containers. 

### 6.1 Installing Docker on our machines
The installation of Docker is more complicated than installing a normal package, for instance over the CLI with apt on Ubuntu.
it is always recommended to follow the newest [Docker Documentation](https://docs.docker.com/desktop/setup/install/linux/ubuntu/) on the offcial Docker webside. 

### 6.2 Creating a Docker file with the necessary dependencies
The task was to create a Dockerfile to build an image. Afterwards, this image can be used to run the code on any machine independent of the operating system.  
We created the Dockerfile manually and didn't use docker-compose, because the Dockerfile of such a small application is short and simple.  
Furthermore, it was a good practice to build the dockefile by hand from scratch. 
If the project becomes more complex we will probably make use of docker compose. 

During the writing of the docker file, the biggest issue was the file itself, but the mounting of the volumes. It took a while to find out how to specify the right paths in the local file system and in the container. 
In the end, three volumes are mounted into the container: datasets, images and models.
These volumes allow the container and the Python code, which runs inside this container to make changes to the filesystem of the local machine.  
It also would have been possible to combine all these directories in one single directory/volume. But in this scenario, the codebase would be nested from our point of view. 

While experimenting with dockerfiles and images. We didn't realize how much space the build images occupy. The result was that after a while almost the entire hard drive was full with iamges. This highlights how important it is to delete unused images regularly.
In the worst-case scenario where no disk space was left the following command was executed, which forces removing all containers, volumes, images, and networks. 
```
docker system prune -a --volumes
```
Normally you would use `docker image prune` to delete all `<none>` images and `docker image prune -a` to delete all unused images.
It is also important to note that all containers related to an image need to be stopped to remove it.  
Moreover, we recognize that our final image is quite large with over two 2GB. We think the main reason for this is the installation of the tensorflow library from which we only used a fraction.
A question for the next lecture would be how to decrease the size of this Docker Image.