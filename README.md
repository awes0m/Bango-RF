# Bango-RF

`B`eginners dj`ango`-`R`est `F`ramework

A simple, yet powerful, django rest framework for beginners.
With Login, Logout, Registration, Password Reset, Password Change, and more.
Also includes Profile, and User Management.

To create a basic Vagrant file of ubuntu image - `vagrant init ubuntu/bionic64` (optional)


## Initial Setup
create a new project with `django-admin startproject {project-name}`
create a new app with `python manage.py startapp {app-name}`

add the {app-name} to the settings.py file in INSTALLED_APPS- this registers the app with the project

Since we are using the django-rest-framework , we should also add the `'rest_framework'` and `'rest_framework.authtoken'` package name in settings.py>INSTALLED_APPS to register the framework with the project

to run the server `python manage.py runserver`


## Create a Model
After defining custom user models, we need to register the user model with the framework.
in the settings.py file, add the following line at teh end:
AUTH_USER_MODEL = '{app-name}.UserProfileManager'

## Migrating the Models to the Database
`python manage.py makemigrations {app-name}` - this creates a migration file for the app
`python manage.py migrate` - this migrates the app to the database. ie- creates the tables needed for the project

## create a Superuser
`python manage.py createsuperuser` - this creates a superuser for the project
it will ask for the username, email, and password.

## register the app with the admin
to register the app with the admin, add the following line to the admin.py file:
`from {app-name}.models import UserProfileManager`
`admin.site.register(UserProfileManager)`

admin site is available at `{server-url}/admin/`

## ApiViews
 Using the rest_framework, we can create a api view to handle the requests.
 the major function of the api view is to handle the requests. namely `get`, `post`, `put`, `delete`, `patch`
 we can us the import
    `from rest_framework.views import APIView` to get the base class for the api view