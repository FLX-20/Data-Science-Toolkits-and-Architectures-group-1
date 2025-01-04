# Milestone 5

## Task 1 Flask Tutorial

## Task 2 Flask Application
The Flask Application was developed independently of the existing backend in a separate container because it only uses the pre-trained model and the existing database. 
In this way, training and production processes are strictly separated from each other.  
But before the development of the actual Flask application started, the code base structure had been designed. This structure is represented in the following code block.
```
app/
├── templates/
│   └── index.html   
├── __init__.py      
├── database.py     
├── model.py         
├── routes.py        
└── utils.py 
```
In the next subsection, this structure and its files are explained in detail.
 
### 2.1 The __init__.py file and Flask Bluebrints
The most important file in the codebase is the `__init__.py` file, which initializes the Flask application and database.
Beside loading the environment variables the `creat_app()` function alos registers the bluebrint.
This structure is the result of experiences of previous Flask projects in the module "Introduction to Computer Science" at the University of Lucern. Here the mistake was that all routes were written in the same file, due to simplicity. However, as the application and its code grew the length of the file also increased, making enhancing and maintaining the codebase more in more difficult.    
For this reason, there are blueprints in Flask, that allow organizing the application into smaller, modular components. This is especially helpful for larger applications. Thus, it is not really required in this small project, because only one blueprint was created. But this structure allows to extend the application quickly with fewer adjustsments.
Furthermore, it increases the redability of the code.  
In the `initialize_database` function an connection to the database is established. On our devices, there is still the problem, that the database connection can not always be established in the first attempt. This was solved, like in the previous milestone by trying it five times. If no connection can be created after five attempts there is are real issue with the connection.

### 2.2 SQLAlchemy and Databases
Instead of using `psycopg2` for interactions with the PostgreSQL database, the Flask application now uses SQLAlchemy. SQLAlchemy is a library that facilitates database interactions by providing tools for Object-Relational Mapping (ORM) and SQL execution. More detailed information on this topic has already been given in the third report. The SQLAlchemy models are defined in the `database.py` file. The database tables and structures remain unchanged from the previous milestones, consisting of the `input_data` and `predictions` tables. The only difference is that these tables are now accessed using SQLAlchemy.

### 2.3 Flask-Routes
All routes of the Flask application are stored in the `routes.py` file. Routes define the URL (endpoints) that a usser cann access to interact with the application. The rout is the mapping between the the URL and the PYthin function, which is executed when the URL is accessed.  
In our application three routes are defined.
- API Route (`/api/predict`) provides a REST API endpoint for predictiong the class of an received image. The input requires an jpg image file in the POST request.  
Then image is processed and a prediction is made. If everything is successful a JSOn object with the predicted label is returned. Otherwise the status code 400 (Bad Reqeust) or 500 (Internal Server Error) is returned. This final api endpoint was test with [postman](https://www.postman.com/), which is a popular tool for testing and debugging APIs, which allowed us to send POST-request to our running application, which included an unseen image. 
- The index page route `/` renders the html page `index.html`, where the user can upload images for prediction.
- The route `predict` handes predictions of images uploaded through the web interface. It works similarly as the `/api/predict` route. However, it is a common choice to separate api and webside routes from each other. It increases modularity and readability of the code. For example this allows to also include flsh functions to show success or error messages on the html page. 

All routes of the Flask application are stored in the `routes.py` file. Routes define the URLs (endpoints) that a user can access to interact with the application. Each route maps a URL to a Python function that is executed when the URL is accessed. In our application, three routes are defined:

- **API Route (`/api/predict`)**: This route provides a REST API endpoint for predicting the class of a received image. The input requires a JPEG image file to be sent in a POST request. The image is then processed, and a prediction is made. If the process is successful, a JSON object containing the predicted label is returned. If there is an error, a status code of 400 (Bad Request) or 500 (Internal Server Error) is returned. This final API endpoint was tested with [Postman](https://www.postman.com/), a popular tool for testing and debugging APIs, which allowed us to send POST requests to our running application, including an unseen image.
- **Index Page Route (`/`)**: This route renders the HTML page `index.html`, where users can upload images for prediction.
- **Prediction Route (`/predict`)**: This route handles predictions for images uploaded through the web interface. It works similarly to the `/api/predict` route. However, it is a common practice to separate API and web routes for increased modularity and readability of the code. This separation also allows for the inclusion of flash functions to display success or error messages on the HTML page.

### 2.4 Running Neural Network
The Flask application uses a pre-trained Neural Network generated by the code of the previous milestones.
The neural network model is loaded by the `load_model()` function in the `model.py` file. Moreover, this file contains the `model_predict` function which runs the model with the received image to return a prediction.
The remaining utility functions, which are not directly related with the neural network are implemented in the `utils.py` file. 
The `process_image_and_predict` is called by both predict routes and includes the entire streamline prediction process.
First the `decode_image` function is called, which converts uploaded image to a 28x28 grayscale numpy array, normalized for the model. But before it is checked if the input come in form of Flask FileStorage class. This class is an abstraction over uploaded files. It provides functionalities like reading the file content, saving the file to a specific location, and accessing metadata such as the filename and content type. If the data doesn't come in this form the subsequnet method `data.read()` will not work.  
The next step in the process of the `process_image_and_predict` function making a prediction with the `model_predict` function.  
Then the metadata of the iamge is stored in the `input_data` table of the database.  
Afterwards the the `save_image_with_uuid` function is called, that save the image on the machine with the same uuid like its metadata in the database.
In the last step the prediction is saved in the `predicition` tabel of the database.
At the end the `prediction` and `image_path` are returned.



The Flask application uses the pre-trained neural network generated in previous milestones. The model is loaded through the `load_model()` function located in the `model.py` file. This file also includes the `model_predict` function, which executes the model using the provided image to return a prediction.

Utility functions not directly related to the neural network are implemented in the `utils.py` file. The `process_image_and_predict` function is called by both prediction routes and encompasses the entire prediction workflow.

The process begins by calling the `decode_image` function, which converts the uploaded image into a 28x28 grayscale numpy array, normalized for the model. Before doing this, it checks whether the input is in the form of the Flask `FileStorage` class. This class abstracts uploaded files and provides functionalities such as reading file content, saving the file to a specified location, and accessing metadata (like the filename and content type). If the data is not in this format, the subsequent method `data.read()` will not work.

Following the image processing, the `model_predict` function is called to generate a prediction. The metadata of the image is then stored in the `input_data` table of the database. Next, the `save_image_with_uuid` function is invoked to save the image on the server, using the same UUID as its corresponding metadata in the database.

Finally, the prediction is saved in the `prediction` table of the database. At the end of the process, the function returns the prediction alongside the path to the saved image.

## Task 3 Frontend

## Task 4 Bringing Everything together 