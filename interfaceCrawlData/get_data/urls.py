from django.urls import path
from get_data import views

urlpatterns = [
	path('', views.hello_world, name='get_data'),
	path('about', views.about, name='get_data')
]