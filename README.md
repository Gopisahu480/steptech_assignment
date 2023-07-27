# steptech_assignment
Implemented Flask API and database functionality

# Flask API Development


The objective of this assignment is to assess your skills and knowledge as a Software Engineer in the areas of Python Flask/Django, MySQL, and Git concepts. You will be required to complete a series of tasks that
simulate real-world scenarios and demonstrate your understanding and proficiency in these technologies.


## Instructions Environment Setup

To deploy this project run

```bash
Install Python 3.x on your machine.
Install Flask using pip: `pip install flask`.
Install MySQL and set up a local database.
```


## the steps to complete the task

#### Step 1:-
Create the below *app.py script(py is the extension to indicate Python script) where we import the flask module. This file should be created under StepTech directory. Notice how we create flask instance.


#### Step 2:-
We create the below *app.py Python script under StepTech  to setup the MySQL database configurations for connecting to database. We need to configure database connection with flask module and that’s why we have imported app module and setup the MySQL configuration with flask module.


#### Step 3:-
Next we need *app.py script under *StepTech  directory.and inside StepTech directory i have created templates folder and inside have user.html and new_user.html.
app.py This script is the perfect instance of Python REST API Developmnt Example using Flask and MySQL. It defines all REST URIs for performing operations. It will also connect to *MySQL database server and query the database to read, insert. Here you can use http PUT method. I have defined only 404 method to handle not found error. You should basically handle required errors, such as, server errors for http responses 500, occurred during the REST API calls.


#### Step 3:-
Create MySQL database table — users with the following structure.
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  role VARCHAR(100)
);

## To access other routes, you can enter the following URLS in your browser.


->
http://127.0.0.1:5000/users - View the list of users from the MySQL database in an HTML table.

->
"http://127.0.0.1:5000/new_user - Add a new user by submitting the form with name email, and role details.

->
"http://127.0.0.1:5000/users/<id> - View the details of a specific user based on their ID.

