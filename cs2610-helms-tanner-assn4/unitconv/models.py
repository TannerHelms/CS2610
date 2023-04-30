from django.db import models


class Convert(models.Model):
    Name = models.CharField(max_length=15)
    Factor = models.FloatField()
