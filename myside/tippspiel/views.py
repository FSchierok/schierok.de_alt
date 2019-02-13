from django.shortcuts import render, redirect
from . import sniffer
from tippspiel.models import Event, Match, Tip, Point
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if "url" in request.GET:
        newEvent = sniffer.newEvent(request.GET.get("url"))
        if newEvent[1] != -1:
            if not Event.objects.filter(title=newEvent[0]).exists():
                E = Event(title=newEvent[0], id=newEvent[1], finished=False)
                E.save()
                for user in User.objects.all():
                    P = Point(user=user, event=E, points=0)
                    P.save()
    return render(request, "tippspiel/index.html", {"running": Event.objects.filter(finished=False), "result": Event.objects.filter(finished=True)})


def event(request, id):  # Event anzeigen
    if request.user.is_authenticated:
        req = request.POST.dict()
        for key in req.keys():
            if key != "csrfmiddlewaretoken":
                tip = key.split(".")
                T = Tip.objects.filter(
                    user=request.user, match=Match.objects.filter(id=tip[0])).first()
                if T == None:
                    T = Tip(user=request.user, tip=bool(
                        int(tip[1])), match=Match.objects.get(id=tip[0]))
                    T.save()
                else:
                    T.tip = bool(int([1]))
        event = Match.objects.filter(event__id__contains=id)
        matches = sniffer.getMatches(id)
        for matchURL in matches:
            match = sniffer.getMatch(matchURL)
            if match["id"]!=-1:
                if not Match.objects.filter(id=match["id"]):
                    M = Match(team1=match["team1"], team2=match["team2"], finished=False,
                            id=match["id"], result1=-1, result2=-1, event=Event.objects.get(id=id), url=matchURL)
                    M.save()
        results=sniffer.getResults(id):
            for result in results:
                match=Match.objects.get(id=int(result[0].split("/")[2]))
                if not match.finished:
                    match.finished=True
                    match.result1 =bool(result[1])
                    match.result2 =not bool(result[1])
                    match.save()
                    for user in User.objects.all():
                        if Tip.objects.get(user=user, match=match).tip == bool(match.result2):
                            Point.objects.get(
                                user=user, event=match.event).points += 1
                            Points.save()

        return render(request, "tippspiel/event.html", {"title": Event.objects.get(id=id).title, "matches": Match.objects.filter(event__id__contains=id, finished=False), "username": request.user.get_username, "points": Point.objects.get(user=request.user, event=Event.objects.get(id=id)).points, "result": Match.objects.filter(event__id__contains=id, finished=True)})
    else:
        return redirect("/u/login")


def result(request, id):
    return render(request, "tippspiel/result.html", {"points": Point.objects.filter(event__id__contains=id)})
