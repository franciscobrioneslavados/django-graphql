# Django Graphql

### Setup folder, a install venv and other dependecies
```
mkdir <root-project>
python3 -m venv venv
source venv/bin/activate
pip install django
pip install graphene-django
pip install django-filter
pip install django-graphql-jwt
pip install django-environ
```
### Create a django projects call core and runs migrations
```
django-admin startproject core .
python manage.py makemigrations
python manage.py migrate
```

### Create a new APP... create a folders before
```
python manage.py startapp students core/apps/students 
python manage.py makemigrations students
python manage.py makemigrations
python manage.py migrate students
```

### Run Server
```
python manage.py runserver
```