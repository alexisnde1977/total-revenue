# coding_challenge

## Overview
This coding challenge is meant to test problem solving, execution, communication, and documentation.  Software building and designing is more of an art than just a skill so be creatvie and have fun.

## Challenge Statement
Build a simple web form that ingests the `data.tsv` file in this repo.  Don't worry about the presentation, it simply has to work.  You can use any language or framework you are comfortable with.  The following requirements are needed for a successful completion:

- Web Application that uploads the `data.tsv`
- Backend persistent system to hold the data (ie. mysql, sql-server, postgress)
- Based on the records in the file calcalute and display to the user the Total Revenue for the records
  - Item Revenue is `item_price * item_count` so a Total would need to be generated and displayed
  - For the given `data.tsv` the total should be `$114802.93`(use this to verify)
- There are 100 records in the data file so you should have 100 records in your backend(FYI,there is a header in the file)
- Handle errors gracefully
- User should have the ability to upload multiple times so provide some page navigation to do so
- You should document everything needed to build your project from scratch(include with the project ie. README).  Assume you are handing this over to someone new so they need all the information to build your entire project(web app, backend, libraries, etc.) and the steps to execute.
- Project can be packaged, emailed, or just use [Github](https://github.com) and share.
- Have fun!

## Summary
This test is meant to test problem solving, creativity, and documentation.  Don't spend more than a couple of hours.  This isn't a pass or fail test we just want to see how our tackle problems and your level of detail.

##### Solution to Challenge #####
In this project I will use Python and Django which is a free and open-source high-level Python web framework designed to help developers build secure, 
scalable and maintainable web applications. I will be using Linux CentoS 8 to accomplish this project.

### SETUP ####
### N.B - Before Starting - Please upload the content(total_revenue) of the zip file to the opt directory and start from there. I have already modified the tsv/views.py to calcalute the Total Revenue and the html files templates/ directory to display output ###

### Install Python3 ####
 ```yum install -y python3```

### Create a folder for the project and CD in to the folder - (I always like to do installations and project in the opt directory. cd /opt)
  ```mkdir total_revenue```
  ```cd total_revenue```

### Create / Launch a Python virtual environment
    Create a Python environment. This is the environment that will enable us to install/configure and run the Django app
```python3 -m venv venv```
    Activate the environment
```source venv/bin/activate```

### Install Django
    This installs the Python module Django that is used to create the web application.
```pip install Django```

###Creating the Project 
    This command creates a Django project named total_revenue 
```django-admin startproject total_revenue```

### Database Setup
Navigate to the total_revenue directory. In this directory we have the manage.py and other files and folders that will help run our webserver
```cd total_revenue```

The two commands below sets up the SQLite3 database with the object model for the Revenue objects (where each row of the tsv is stored)
```python manage.py makemigrations tsv```
```python manage.py migrate```

### Create Admin Account
Create an administrator account. This will be used to view the database.

```python manage.py createsuperuser```
The above command will be prompted to answer an array of questions. 
Username (leave blank to use 'root'): alexis
Email address: alexis@domain.com
Password:
Password (again):
Superuser created successfully.)

### Run Server
This is the command that actually runs the Django server (http://localhost:8000) - assuming port 8000 is open
```python manage.py runserver```

Navigate to http://localhost:8000.
To view the SQLite3 database, navigate to http://localhost:8000/admin. with username and password created from command above

### Deactivating the Virtual Environment
This command deactivates the environment once we are done with the work.
```deactivate```

### Database Documentation

### Revenue
Item: Character Field (max length of 100)

Item Description: Character Field (max length of 200)

Item Price: Decimal Field (2 decimal places and max digits of 20)

Item Count: Integer Field

Vendor: Character Field (max length of 100)

Vendor Address: Character Field (max length of 200)

### I have attached screenshots of the final product. Thanks Alexis Nde
