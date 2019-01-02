from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "tippspiel/index.html")


def newEvent(request):  # Neues Event anlegen
    return False


def event(request):  # Event anzeigen
    return render(request, "tippspiel/event.html", )
