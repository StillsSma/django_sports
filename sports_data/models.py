from django.db import models

# Create your models here.

class Corn_husker(models.Model):
    Player = models.CharField(max_length=20)
    Att = models.IntegerField()
    Yrds = models.IntegerField()
    Avg = models.FloatField()
    TD = models.IntegerField()
