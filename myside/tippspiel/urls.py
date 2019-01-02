from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(r"", views.index, name="Tippspiel"),
    path(r"nesevent", views.newEvent, name="Neues Event"),
    path(r"event/\d+", views.event)
]
