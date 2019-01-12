from django.shortcuts import render


def index(request):
    return render(request, "home/home.html")


def login(request):
    return render(request, "home/login.html")
