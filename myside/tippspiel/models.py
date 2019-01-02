from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=128)
    id = models.IntegerField(primary_key=True)


class Match(models.Model):
    team1 = models.CharField(max_length=64)
    team2 = models.CharField(max_length=64)
    finished = models.BooleanField()
    result1 = models.IntegerField()
    result2 = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)


class User(models.Model):
    nick = models.CharField(max_length=64)
    salt = models.CharField(max_length=64)
    hash = models.CharField(max_length=64)


class Tip(models.Model):
    match = models.ForeignKey("Match", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    tip = models.BooleanField()
