# Bango-RF

`B`eginners dj`ango`-`R`est `F`ramework

A simple, yet powerful, django rest framework for beginners.
With Login, Logout, Registration, Password Reset, Password Change, and more.
Also includes Profile, and User Management.

To create a basic Vagrant file of ubuntu image - `vagrant init ubuntu/bionic64` (optional)

create a new project with `django-admin startproject {project-name}`
create a new app with `python manage.py startapp {app-name}`

add the {app-name} to the settings.py file in INSTALLED_APPS- this registers the app with the project

Since we are using the django-rest-framework , we should also add the `'rest_framework'` and `'rest_framework.authtoken'` package name in settings.py>INSTALLED_APPS to register the framework with the project

to run the server `python manage.py runserver`