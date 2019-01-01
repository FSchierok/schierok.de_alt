from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("overpass", views.overpass, name="Overpass"),
    path("overpass/small", views.overpass_small,
         name="Overpass small Downlaod"),
    path("overpass/HD", views.overpass_HD, name="Overpass HD Download"),
    path("train",views.train, name="Train Download"),
    path("inferno",views.inferno,name="Inderno Download"),
]
