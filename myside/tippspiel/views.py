from django.shortcuts import render, redirect
from . import sniffer
from tippspiel.models import Event, Match, Tip, Profil

# Create your views here.


def index(request):
    if "url" in request.GET:
        newEvent = sniffer.newEvent(request.GET.get("url"))
        if newEvent[1] != -1:
            if not Event.objects.filter(title=newEvent[0]).exists():
                E = Event(title=newEvent[0], id=newEvent[1])
                E.save()
    return render(request, "tippspiel/index.html", {"running": Event.objects.all()})


def event(request, id):  # Event anzeigen
    if request.user.is_authenticated:
        req = request.POST.dict()
        for key in req.keys():
            if key != "csrfmiddlewaretoken":
                tip = key.split(".")
                print(tip)
                T = Tip(user=request.user, tip=bool(
                    tip[1]), match=Match.objects.get(id=tip[0]))
                T.save()
        event = Match.objects.filter(event__id__contains=id)
        matches = sniffer.getMatches(id)
        for matchURL in matches:
            match = sniffer.getMatch(matchURL)
            if not Match.objects.filter(id=match["id"]):
                M = Match(team1=match["team1"], team2=match["team2"], finished=False,
                          id=match["id"], result1=-1, result2=-1, event=Event.objects.get(id=id), url=matchURL)
                M.save()
        for match in event:
            if not match.finished:
                result = sniffer.getResult(match.url)

                if result[0]:
                    match.finished = True
                    match.result1 = bool(result[1])
                    match.result2 = not bool(result[1])
                    match.save()
                    for profil in Profil.objects.all():
                        if Tip.objects.get(user=profil.user, match=match).tip == bool(match.result2):
                            profil.points += 1

        return render(request, "tippspiel/event.html", {"title": Event.objects.get(id=id).title, "matches": Match.objects.filter(event__id__contains=id, finished=False), "username": request.user.get_username, "points": Profil.objects.get(user=request.user).points, "result": Match.objects.filter(event__id__contains=id, finished=True)})
    else:
        return redirect("/u/login")
