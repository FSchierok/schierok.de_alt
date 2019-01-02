from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from rgnbgn.models import Doc


def index(request):
    return render(request, "rgnbgn/rgnbgn.html", {"entries": Doc.objects.all()})


def overpass(request):
    try:
        response = HttpResponse(open("rgnbgn/html/overpass.html"))
        return response
    except FileNotFoundError:
        raise Http404()


def overpass_small(request):
    try:
        response = FileResponse(
            open('rgnbgn/overpass_small.pdf', 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = "attachment; filename=overpass_small.pdf"
        return response
    except FileNotFoundError:
        raise Http404()


def overpass_HD(request):
    try:
        response = FileResponse(
            open('rgnbgn/overpass_HD.pdf', 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = "attachment; filename=overpass_HD.pdf"
        return response
    except FileNotFoundError:
        raise Http404()


def inferno(request):
    try:
        response = FileResponse(
            open("rgnbgn/inferno.pdf", "rb"), content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename=inferno.pdf"
        return response
    except FileNotFoundError:
        raise Http404()


def train(request):
    try:
        response = FileResponse(
            open("rgnbgn/train.pdf", "rb"), content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename=train.pdf"
        return response
    except FileNotFoundError:
        raise Http404()
