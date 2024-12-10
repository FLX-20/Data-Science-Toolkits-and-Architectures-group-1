# Milestone 3

## Task 1 - Setting Up Docker Compose








## Task 2 - Simple PostgreSQL Application








## Task 3 - Loading and Saving Images in PostgreSQL Database







## Task 4 - Multi-Docker Container Application



## Little project riddles (optional)

### 1. SQL Injection Attack
An SQL Injection attack happens when hackers trick your website into running harmful code in the database by typing 
unexpected inputs, like special characters or commands, into fields like login forms. This could let them steal 
data, bypass login, or even delete important information.

#### An example of a SQL Injection Attack:
SELECT * FROM users WHERE username = 'user' AND password = 'pass';

If a hacker enters `user' OR '1'='1` as the username, the query becomes:
SELECT * FROM users WHERE username = 'user' OR '1'='1';

This always returns true, letting them log in without the right password.

#### How to protect yourself against a SQL Injection Attack
1. Use Safe Query Methods:
   cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, password))
2. Check Inputs: Make sure inputs only allow expected characters (e.g., no `--` or `'`).
3. Restrict Database Access: The website’s database account should only have limited permissions.
4. Test for Vulnerabilities: Regularly check for weaknesses using tools like SQLmap.

### 2. Difference Between Relational Database (RD) and a Document Store (DS)

#### Relational Database:
Relational Database stores data in `tables` with rows and columns, like a spreadsheet. It has a fixed structure, so the data must fit a specific format (e.g., numbers, dates). Examples of RD are MySQL or PostgreSQL.

#### Document Store:
Document store stores data as `documents`, like JSON files. Each document can look different. It is very 
flexible, so you do not need a strict structure. This is great for unstructured or changing data. Examples of DS are MongoDB or CouchDB.

#### 2.1 Scenarios Where You Should Use Relational Database:
You should use RD when data is highly structured, and relationships matter, like in finance, 
healthcare, or HR systems where you need consistency and complex queries.

#### 2.2 Scenarios Where You Should Use Document Store:
You should use DS when data is less structured or needs flexibility, such as handling product catalogs, 
user profiles, or social media posts where schema might change frequently.

### 3. SQL Join Operation
A SQL Join combines data from two or more tables when they have a common link. Same as merging two datasets with
one common column variable. 

#### Types of Joins + Examples:
1. **INNER JOIN**: Only shows matching data from both tables.
   SELECT employees.name, departments.name
   FROM employees
   INNER JOIN departments ON employees.dept_id = departments.id;

2. **LEFT JOIN**: Shows everything from the first table and matches from the second table (or `null` if there’s no match).
   SELECT employees.name, departments.name
   FROM employees
   LEFT JOIN departments ON employees.dept_id = departments.id;

3. **RIGHT JOIN**: Opposite of LEFT JOIN—shows all data from the second table and matches from the first table.
   SELECT employees.name, departments.name
   FROM employees
   RIGHT JOIN departments ON employees.dept_id = departments.id;
