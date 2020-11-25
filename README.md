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
Then create function name: nameFunctionOne. That function will call file nameOfFileHtml.html 
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

## Add bootstrap, css or script
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
```bash
scrapy startproject nameOfProject
```
## License
[KVU](https://github.com/kvu-luong)