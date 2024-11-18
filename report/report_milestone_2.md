# Milestone 2

## 1 Establishing a Clean Git Repository



## 2 Technical Concepts and Tool Preferences

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



## 4 Code Modularization and Structure Enhancement



## 5 Dependency Management with pip and Virtual Environments



## 6 Containerizing the Application with Docker