from . import views
from django.urls import path

app_name = 'escolaine'

urlpatterns = [
	  path('', views.index, name = 'index'),
	]