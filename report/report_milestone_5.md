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





## Task 3 Frontend

## Task 4 Bringing Everything together 