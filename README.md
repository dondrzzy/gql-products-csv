# Simple GraphQL project to read products

## Prerequisites
- django
- graphene

## Setup

This project uses the default sqlite3 database

Run 
```py
# set up database
python manage.py makemigrations
python manage.py migrate

# load dummmy data
python gqlapp/scripts/load_data.py 

# start the server
python manage.py runserver

# go to 
http://localhost:8000/graphql
```