from django.db import models


class Doc(models.Model):
    map = models.CharField(max_length=16)
    author = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    file = models.FileField()
