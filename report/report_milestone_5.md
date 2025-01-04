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






## Task 3 Frontend

## Task 4 Bringing Everything together 