from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name="Home"),
    path('addTask', views.appendTask,name="appendTask"),
    path('deleteTask/', views.deleteTask,name="Deleting task"),

]