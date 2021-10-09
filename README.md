

# Capstone Project - restock_checker 
**Danny Li, Alden Lee, Ethan Tam, Oscar Andrade, David Xue**

# Django Section


To run server, run the command:
"python manage.py runserver "

Note: can add a port number in front of runserver to connect to a particular port, else defaults to port 8000

requires:

pip install django

pip install python-decouple

pip install mysqlclient

(you will also need to have MYSQL installed as we'll be using MYSQL for our database)

Note: you'll also need to set your mysql username to **root** , mysql password to **password** and have a mysql database called **restock** 

To get the all tables into your database, run the command:
"python manage.py migrate"