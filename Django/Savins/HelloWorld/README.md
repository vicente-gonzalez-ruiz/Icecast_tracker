# Implementation of a HelloWorld app with Django in Ubuntu.

The steps are:

1. Install Python.
2. Install Django.
3. Create a HelloWorld app.
4. Deploy it.


# 1. Install Python

As Django is a framework of Python, we need install python first (if you have it installed, skip this step).

First, we need install some dependencies:
~~~
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
~~~

Second, we download python *.tgz file, extract and install.
~~~
cd ~/Downloads/
wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz

tar -xvf Python-2.7.5.tgz
cd Python-2.7.5

./configure
make
sudo checkinstall
~~~

Finally, to verify Python is installed, we run the following command:

~~~
python
~~~


# 2. Install Django

Once we have installed Python, we can install Django. For that, we need to install *PIP (Python Package Index)*:
~~~
sudo apt-get update
sudo apt-get install python-pip
~~~
And then, we install Django:
~~~
sudo pip install django
~~~

When the process finish, we verify the installation with:

~~~
django-admin --version
~~~

# 3. Create a HelloWorld app.

Let's create a HelloWorld  project:
~~~
django-admin.py startproject HelloWorld
~~~

The folder structure that is create is:
~~~
HelloWorld
├── HelloWorld
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
~~~

* __init__.py
	: An empty file that tells Python that this directory should be considered a Python package.
* settings.py
	: Settings/configuration for this Django project. Django settings will tell us all about how settings work. In other words, this file will hold all apps, database settings information.
* urls.py
	: The url declarations for this Django project; a "table of contents" of our Django-powered site. This is a file to hold the urls of our website such as "http://localhost/HelloWorldApp". In order to use /HelloWorldApp in our HelloWorld project we have to mention this in urls.py.
* wsgi.py
	: An entry-point for WSGI-compatible web servers to serve our project. This file handles our requests/responses to/from django development server.

# 4. Deploy it:

We run the development server:
~~~
python manage.py runserver
~~~

Finally, open a browser and go "http://127.0.0.1:8000/", then we get the default page.

***
***
# Extesion using routes and adding a new project.

New apps in Django are similar to modules. The following steps focus on adding a new project and assigning routes to its views. So, we start creating a new application. 

# 1. Create new app.

~~~
django-admin startapp TimeServerApp
~~~

The new folder structure is:
~~~
HelloWorld
├── HelloWorld
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── TimeServerApp
│   ├── admin.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
~~~

* __init__.py
	: this file indicates our app as python package.
* models.py
	: file to hold our database informations.
* tests.py
	: for testing.
* views.py
	: our functions to hold requests and logics.

# 2. Configure the project.

We need to edit settings.py to add the application TimeServerApp:

~~~
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TimeServerApp',
)
~~~

Django has a way to map a requested url to a view which is needed for a response via regular expressions.

Let's modify the urls.py.

```python
from django.conf.urls import patterns, include, url
from TimeServerApp.views import foo

urlpatterns = patterns('',
    url(r'TimeServerApp/$', foo),
)
```

Finally, we modify the view. In this case, views.py.

```python
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def foo(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```

# 3. Deploy the new app.
Like case before, we run the server with:

~~~
python manage.py runserver
~~~

And we access to "http://127.0.0.1:8000/ServerTimeApp/"

![example](https://github.com/Sistemas-Multimedia/Icecast-tracker/blob/master/Django/Savins/public/images/example.png)
