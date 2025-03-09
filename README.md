# BOOKSPREN 

## Clone Repo
git clone https://github.com/StressSpren/Book_Shop.git

## Entering virtual environment
./venv/Scripts/activate

## Apply migrations when changing database fields
py manage.py makemgrations 
py manage.py migrate

## Create a superuser to access admin page
py manage.py createsuperuser

## Run local server 
py manage.py runserver

## Base Directory
cd django_project


# Usage Guide
Users will have the ability to register and log in, browse books by category and add items to a cart system within an SQLite3 database. Admins will be the only users able to add, edit and delete books, accessed through the admin panel.

## Access Admin panel
127.0.0.1:8000/admin 

## Access SQLite3 Database 
sqlite3 db.sqlite3

## Open a python shell to test the data
py manage.py shell

# Testing

e.g. py manage.py test apps.api.test


