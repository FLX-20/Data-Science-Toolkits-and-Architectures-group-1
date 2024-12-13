# Milestone 3

## Task 1 - Setting Up Docker Compose








## Task 2 - Simple PostgreSQL Application

a) What is PostgreSQL? SQL or NoSQL
It is a RDBMS, which is short for relational database management system - it uses SQL, which is short for structured query language to access, define and manipulate data. Furthermore the ACID structure, referring to the data points being Atomic, Consistent, Isolated and Durable is another sign for the SQL nature of PosegreSQL. As such it is SQL as the data is stored in a structured way in tables with rows and columns and Primary as well as Foreign Keys are utilized.

b) If the container was stopped  and started again the joke would still be in the Database, yes, because the data memory is not-volatile, meaning it can persist through restarts or even power outtages. This means that the joke will still persist, as it does after one has used "stop" and "start" commands to restart the container, because docker volumes remain even after the corresponding container stops. 

## Task 2.1 - Documentation on the joke database

In order to run a PostgreSQL Server via a docker image we need to download, or rather pull, the most recent available PostgreSQL image. This is done via the command: “docker pull postgres:latest”

Subsequently, we need to run the PostgreSQL container. Setting the following parameters of the Username and Password being admin and creating a test database named “testdb” we assign the port 5432 to the container and map it to the same number port of the localhost. Furthermore we assign the name “PostgreSQL-container” for better identification.

Afterwards we create the python file, in this case we call it “joke_database.py”. The corresponding script contains first the credentials of the to access database (User, Password, Port, like discussed above). We proceed to connect to the database via the parameters we just set in the step before, and begin to create  a table in the database, which will subsequently get filled with Jokes, and their corresponding IDs.


Furthermore we add 4 functions that carry out the following acts:

1. “add_joke” inserts a joke into the table
2. “delete_joke_by_id” allows us to remove one of the jokes without having to write it out entirely, but just by providing its corresponding ID
3. “get_all_jokes” fetches all jokes simultaneously from the table
4. “Modify_joke” allows us to temper with the content of a respective joke and alter it, by accessing it via its ID

Afterwards we execute the python script via “python joke_database.py” and get the following, expected, output: 

“Connected to the database successfully.
Table 'jokes' created.
Connected to the database successfully.
Joke added with ID: 1
Current jokes in the database:
Connected to the database successfully.
ID: 1, Joke: Why don't scientists trust atoms? Because they make up everything!”


## Task 3 - Loading and Saving Images in PostgreSQL Database







## Task 4 - Multi-Docker Container Application








