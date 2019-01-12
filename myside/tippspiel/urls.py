from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(r"", views.index, name="Tippspiel"),
    path(r"event/<int:id>", views.event),
]
