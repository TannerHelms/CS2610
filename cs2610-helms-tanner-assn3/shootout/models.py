from django.db import models


class Expressions(models.Model):
    firstOperand = models.FloatField()
    operator = models.CharField(max_length=1)
    secondOperand = models.FloatField()
    total = models.FloatField(null=True)
    date_created = models.DateTimeField('Date Posted')
