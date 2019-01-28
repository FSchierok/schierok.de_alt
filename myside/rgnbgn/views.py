from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from rgnbgn.models import Doc


def index(request):
    if request.user.groups.filter(name='rgnbgn').exists():
        return render(request, "rgnbgn/rgnbgn.html", {"entries": Doc.objects.all()})
    else:
        raise Http404
