from django.contrib import admin
from django.urls import path
from . import views

app_name = 'taskcatalog'

urlpatterns = [
    path('', views.taskList, name='tasks'),
]
