from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Expenses(models.Model):
    date = models.DateTimeField('date published')
    amount = models.FloatField(default=0)