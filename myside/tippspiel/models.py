from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=128)
    id = models.IntegerField(primary_key=True)
    finished = models.BooleanField()

    def __str__(self):
        return self.title



class Match(models.Model):
    team1 = models.CharField(max_length=64)
    team2 = models.CharField(max_length=64)
    finished = models.BooleanField()
    result1 = models.IntegerField()
    result2 = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.team1 + "_vs_" +self.team2


class Tip(models.Model):
    match = models.ForeignKey("Match", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.BooleanField()
    
    def __str__(self):
        return self.user +":_"+ self.match


class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    points = models.IntegerField()
