# Basic selenium setup
- download python: [Python](https://www.python.org/downloads/) 
- setup enviroment variable -> link to folder contain python.exe. [reference](https://www.educative.io/edpresso/err-python-is-not-recognized-as-an-internal-or-external-command)
- install selenium for python: 
```bash 
python -m pip install selenium
```

## To open Chrome
1. install package chromedriver-binary
```bash
python -m pip install chromedriver-binary
```
2. import package
```bash
import chromedriver_binary
```

# Build interface with Django
[reference](https://realpython.com/get-started-with-django-1/)
## Setup project
1. Install virtual enviroment working with python
```bash
python -m venv venv
```
2. Activate env on window
```bash
source venv/Scripts/activate 
```
3. Install Django
```bash
(venv) $ pip install Django
```
4. Create project
```bash
django-admin startproject nameOfProject
```
5. Clear up project
```bash
mv nameOfProject/manage.py ./
mv nameOfProject/nameOfProject/* nameOfProject
rm -r nameOfProject/nameOfProject
```
6. Run server
```bash
python manage.py runserver
```

## Create app in project with Django
1. Create app
```bash
python manage.py startapp nameOfApp
```
2. Let project know app exist
Path: nameOfProject/settings.py
Tab: INSTALLED_APPS

### Create view
Path: nameOfApp/views.py  
Then create function name: nameFunctionOne.   
That function will call file nameOfFileHtml.html 
```bash
def nameFunctionOne(request):
	return render(request, 'nameOfFileHtml.html', {})
```
1. Create html file in templates folder of app
```bash
mkdir nameOfApp/templates/
touch nameOfApp/templates/nameOfFileHtml.html
```
2. Register url to render html in project
Path: nameOfProject/urls.py  
Then add name library
```bash
from django.urls import path, include

urlpatterns = [
	path('', include(nameOfApp.urls)) #home page
]
```
3. Register url to render html in app
If this is the first time, we need to create file urls.py in app
```bash
touch nameOfApp/urls.py
```
In nameOfApp/urls.py. We register url for render file nameOfFileHtml.html
```bash
from nameOfApp import views #first time
urlpatterns = [
	path('', views.nameFunctionOne, name='nameOfApp')
]
```
to call another file html we just need to define another function which call to another file html.
```bash
path('otherPath', views.nameOtherFunction, name='nameOfApp')
```

*** Remember: Declare templates url in nameOfProject/setting.py like ```nameOfProject/templates```

### Setup Model connect to database
Remember: manage.py have to place parallel with project folder
makemigrations: create schema for database from model
migrate: generate database
```bash
python manage.py makemigrations
python manage.py migrate
```
### Add bootstrap, css or script
1. Create file load html and js like header file
Path: nameOfProject/templates
```base
mkdir nameOfProject/templates/
touch nameOfProject/templates/header.html
```
in header.html we call css, js and block of other file like this
```bash
<link rel="stylesheet" href="" type="text/css">
{% block page_content %} {% endblock %}
<script src=""/>
```
to call file header.html in other file 
```bash
{% extends "header.html" %}
{%block page_content %}
	<div>Content of other file</div>
{% endblock %}

```
2. Add static file like css, js, image
Create folder name 'static' then create file in this forder of App.  
Path: nameOfApp/static
```bash
mkdir nameOfApp/static
touch nameOfApp/static/fileCssStatic.css 
```
Then call it in template
```bash
{% load static %}
<link rel="stylesheet" type="text/css" href={% static 'fileCssStatic.css' %}
```
Usually, we call it in file header, so we just need to call it one time.  
3. For CND link like bootstrap  
We just copy link and paste it to header.html

## Scrapy
Crawl data for auto tool

### Setup virtual enviroment
1. Install venv
2. Active enviroment venv
```bash
 source venv/Scripts/active
```
2. instal scrapy
```bash
pip install scrapy
```

### Create spider for crawl data
[Reference](https://docs.scrapy.org/en/latest/intro/tutorial.html)
1. Create project
```bash
scrapy startproject nameOfProject
```
2. Run crawl
```bash
scrapy crawl nameOfSpider
```

## Ajax with Django
[Reference](https://www.pluralsight.com/guides/work-with-ajax-django)
WorkFlow
1. Create model contains all field that we need in nameOfApp/models.py
2. Create form at backend nameOfApp/forms.py
3. Pass all data of Form and Model to view which we need in nameOfApp/views.py
```bash
from django.http import JsonResponse
from django.core import serializers
from .forms import nameOfForm
from .models import nameOfModel
```
4. At front-end, we render all field of form and write ajax function in nameOfApp/templates/index.html
5. Define url ajax function in nameOfProject/urls.py which we already created.
Method 1:
```bash
path('post/ajax/specificName', nameOfFunction, name='urlNameCall'),
```
'post/ajax/specificName' can be any string we want. Just use for make distinct between other url.

In interface we view call function like below
```bash
$.ajax({
	type: 'POST',
	url: "{% url 'urlNameCall' %}",
	data: dataSerializedData,
	success: functin (rs){

	},
	error: function(rs){

	}
})
```
Method 2:
Define nameOfApp/views.py as View
```bash 
from django.views import View
```
Then, in nameOfProject/urls.py, change path to
```bash
 path('', nameOfClass.as_view(), name="urlNameCall"),
 ````
## License
[KVU](https://github.com/kvu-luong)