Implementation of a project using Django in MAC
================================================

Step 1 - Install Python y Django
--------------------------------
We can see that Python is yet installed in MAC running the command "python" at the terminal.
~~~
$ python
~~~
Next, we install **Pip** (is a package management system used to install and manage software packages written in Python)
~~~
$ sudo easy-install pip
~~~
Then, we install **Django** 
~~~
$ sudo pip install django
~~~
Step 2 - Creating the Project 
--------------------------------------------------
First of all, we install setup.py
~~~
$ python setup.py install
~~~
And then we create the project
~~~
$ django-admin.py startproject holamundo333
~~~
Next, we enter the location of the project, and we create the application in Django
~~~
$ python manage.py startapp saludo333
~~~
And, finally, we run the server
~~~
$ python manage.py runserver
~~~
Step 3 - Creating the Application
----------------------------------
To tell Django a new application exists, we modify the file **settings.py**, adding to the array "INSTALLED_APPS" the name of our application
~~~
INSTALLED_APPS=(
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.conttentypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'saludo333')
~~~
Next, we create the *templates* folder at the root of the project and modify the file **settings.py** again
~~~
TEMPLATES = [{
  ...
  'DIR':[BASE_DIR+"/templates",],
  ...
}]
~~~
Then, we create a url in Django. We edit the file **urls.py** adding:
~~~
url(r'^holamundo/$','saludo333.views.saludo');
~~~
Now we have to open the file views.py and add the function that will create the greeting we view
~~~
from django.shortcuts import render #importamos render de django

# Create your views here.

def saludo(request):    # nombre saludo que se pone para llamar a la vista 
					    # url(r'^holamundo/$','saludo333.views.saludo'),
	nombre = "Roci"
	tupla = (1,2,3,4,5,6,7,8,9,10);
	context = {
		'saludo':'Hello, how are you?',
		'tupla':tupla,
		'nombre':nombre
	}
	#devolveremos los datos a la vista saludo.html para printarlos
	return render(request,'saludo3.html',context)
~~~
Finally, we create the file **saludo.html** and adding to the file templaes
~~~
<html>	
	<html>
	<head>
		<title>Hola mundo 333 con Django</title>
	</head>
	<body>
		{{ saludo }}<br>
		{% for datos in tupla %}
			{{ datos }}<br>
		{%endfor%}
	</body>
</html>
~~~
Now we are running the server again and access the url
~~~
http://127.0.0.1:8000/holamundo
~~~



