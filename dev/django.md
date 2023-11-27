# Django

## Installation

You can install *Django* with `pip install django`. Use `python -m django --version` to make sure
Django is installed and check which version of it is.

## Project

Run `django-admin startproject {projectName}` to generate a Django project. When choosing a name
for your project, bear in mind you should avoid names that might conflict with Django (like
'django' itself) or with Python (like 'test', the name of an existing built-in Python package).

This code should not live under a web server's document root (something like */var/www*) as in plain
old PHP with no framework. Doing this is actually not good for security since people might be able
to view the code then. Just put this code elsewhere, such as in your home folder.

## Development Server

Django includes a development server for rapid development and testing. You can launch it with 
`python manage.py runserver`. As its name indicates, it is in no way intended for production.

## REST

- To use Django as a REST API, you can first include the `djangorestframework` dependency in your
  requirements.txt and install it.
- Then you must add `'rest_framework'` in the settings file's *INSTALLED_APPS* key
- You can also add the line `path('api-auth/', include('rest_framework.urls'))` to the *urls.py* file
  to enable the authentication system