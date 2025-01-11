# Milestone 5
In the beginning, the fifth milestone was divided into two main tasks. 
The first task involved developing the Flask application, which includes both the API and the web frontend. This is described in detail in chapters two and three.  
The second part of the milestone focused on adjusting the backend, which was developed over the previous four milestones. Our backend was designed to classify any image dataset from external sources. However, for the current milestone, we only need to classify the MNIST images, which are already included in the Keras package.   
Thus, the entire codebase can be simplified since all functions related to reading external data are no longer necessary. If those functions are needed again, they can be retrieved from the git history. This decision was made to make the application as lightweight as possible and avoid unnecessary code that does not contribute to the productive code.  
Additionally, the Flask application and the modified backend are merged in the end to create a coherent web application consisting of several containers.
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
The frontend presented to the user is defined in the `index.html` file located in the `templates` directory. This file make use of the Bootstrap framework for styling and layout, which provides a variety of pre-styled components and a responsive grid system. The decision to use Bootstrap was made, because of prior experience with the framework from past projects.    
By assembling components from the Bootstrap [documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/), we were able to create an adaptive and user-friendly interface without the need for additional CSS or JavaScript files.    
Additionally, the templating engine Jinja is used in this file to dynamically change content on the HTML page. It manages the rendering logic based on the data passed from the Flask backend. Jinja's `{{ ... }}` syntax is applied to embed Python variables or expressions.  For instance, this is used to return the prediction value.    
Furthermore, Jinja uses `{% ... %}` blocks for control logic, such as loops and conditionals. For example, we used these blocks to render only the lower part of the page when a prediction was returned.  
The remainder of the `index.html` file consists of standard HTML code, which provides the webpage with its structure.

## Task 4 Production Architecture
During the entire development phase, the system was tested on the local Flask development server. However, this server is not suitable for production for several reasons. For instance, the Flask development server is single-threaded by default, which means it can only handle one request at a time. As a result, it is not capable of serving multiple users simultaneously. Additionally, it does not support load balancing, a feature often necessary for large-scale applications.  
Moreover, the Flask server is not optimized for high performance. It is designed for testing and debugging purposes. Thus, it lacks security features, making it vulnerable to various attacks.  
For these reasons, Gunicorn and Nginx were introduced in the lecture. Gunicorn is a Python WSGI HTTP server. A WSGI (Web Server Gateway Interface) HTTP server acts as an intermediary between our web application (written in Python) and a web server. It provides a standardized interface for Flask-Python web applications to communicate with web servers.  
We installed Gunicorn using the following command:  
```shell
pip install gunicorn
```
Afterwards the CMD in der dockerfile was change:  
```Dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
```
The Command runs the Flask application using Gunicorn, which listens on port 5000 and instantiates two worker processes. These workers allow the application to handle multiple requests concurrently. It is also possible to create an additional configuration file for Gunicorn to enable more complex configurations. This was not necessary in this project due to the simplicity of the application.  
Moreover, Nginx has been configured as a web server designed to efficiently handle high traffic loads. It acts as a reverse proxy for the web service, forwarding incoming HTTP requests from clients (e.g., browsers) to the backend application running on port 5000. Clients interact only with Nginx on port 8080, which enhances the security and organization of the application.  
If we run multiple instances of our web service, Nginx can distribute traffic among them to manage several requests effectively. Furthermore, Nginx serves as a centralized access point, making traffic monitoring easier.  
In this final milestone, the integration and setup of Nginx posed the biggest challenge due to its numerous features and capabilities. Therefore, we opted for the simplest implementation in the `nginx.conf` file, given the small size of the project. Moreover, an additional Docker container was defined for Nginx in the Docker Compose file.
  
The final flow of requests from our understanding is as:
- client sends a request to `http://localhost:8080`
- nginx listens to port `8080`, which is mapped to port 80 in the container
- nginx configuration nginx.conf routes requests to `ttp://web:5000`, which is the Flask app in the `web` container
- The `web` service is running a Gunicorn server (defined in the CMD in the Dockerfile)
- Gunicorn passes requests to the Flask application using the WSGI protocol.
- In `web` Flask processes the request, generates a response, and sends it back to Gunicorn.
- Gunicorn receives the response from Flask and sends it back to NGINX
- Then, in the end, nginx forwards the response to the client

## Task 4 Bringing Everything together 
Additionally, our existing backend had to be adjusted to meet the requirements of the last milestone. We initially expected to obtain an unknown dataset from the web, which contained images that we needed to classify using our CNN architecture. However, it turned out that the final goal was much simpler and focused on the MNIST dataset, which is already included in the Keras library. Consequently, there was no need for direct downloads from the web, making the download and unzip procedures unnecessary. As a result, we decided to delete the related functions.   
One could argue for keeping this function in the code for future modifications, but we believe that code not contributing to the production version should be excluded, as it can introduce potential errors.   
Furthermore, all classification functions were deleted and moved to the front-end Flask application. The backend now solely concentrates on training the CNN and saving the images along with their metadata in the database. These deletions of unnecessary functions significantly simplified the backend.

In this backend adjustment process, one performance issue from the last milestone was identified. In previous code versions, images were used for training and testing almost immediately after being loaded, without much preprocessing. This approach worked well with the smaller animal training dataset (consisting of 300 cats, 300 dogs, and 300 snakes), but it caused program crashes when using the MNIST dataset, which contains 70,000 images.  
To address this issue, we created a TensorFlow dataset that randomly shuffles the training data, batches the dataset for more efficient processing, and prefetches data to enhance performance during training. This implementation helps prevent crashes and speeds up the training process.

When adjusting the backend, it is important to consider how to handle newly added, unlabeled data. This data is provided by users, either through uploads on the website or via the API. Like any other data, it is added to the `input_data` and `prediction` tables.   
For this data, the label is defined as "unknown." To observe all user-uploaded data, you can use the following SQL command:
```sql
SELECT * FROM input_data WHERE label = 'unknown'
```
After identifying the unlabeled data, you can manually label the newly provided data to increase the training dataset size. However, the column `is_training` contains a binary value, where `TRUE` (1) indicates that all newly added data is automatically classified as training data. This approach can lead to issues because the algorithm expects 10 classes, not 11 (with "unknown" being the 11th class), and does not know how to handle the "unknown" class. Therefore, it is necessary to filter out all rows labeled as "unknown" beforehand.  
This filtering can be achieved with the function `fetch_label_map()`, which retrieves and processes label information for a specified set of UUIDs while excluding any invalid entries with the label "unknown." This ensures that only valid data (i.e., those with non-unknown labels) is used for model training or evaluation.  
Subsequently, the model training is performed using the weights and bias procedure developed in the previous milestone. Additionally, a confusion matrix is generated for the final model, along with an overview image of all classes. Both of these images are saved in the `images` directory. The trained model is stored in the `models` directory, from which it is loaded by the Flask application.

## Task 5 Limitation of the project
One significant downside of the current application is that it allows any kind of image to be uploaded, including non-digit images, such as pictures of cats and dogs. However, the forward-passing classification algorithm of the Convolutional Neural Network (CNN) will always classify each image as one of ten digits, regardless of the content. As a result, it is possible for a cat image to be classified as a "9" because, in the world of the CNN, there are only digits and no cats.  
This is a well-known problem in the field of Data Science. For this reason, various researchers have introduced different methods of uncertainty measurement. Uncertainty measures can help identify situations where the model is unsure about its prediction, such as when it encounters a cat image but has only been trained on digit images. This understanding is crucial to avoid naive decision-making that could lead to severe consequences.  
An excellent overview of this topic was provided by [Jakob Gawlikowski](https://arxiv.org/abs/2107.03342) and his colleagues, who introduced multiple strategies to address this issue in their paper.

## Appreciation
As we reach the final milestone of this subject, we would like to take this opportunity to thank you for your efforts in designing and providing this course. It has provided valuable hands-on experience in setting up a data science application and has conveyed essential knowledge that can serve as a foundation for future private projects.