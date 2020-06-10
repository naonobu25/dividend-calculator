from django.db import models
from django.conf import settings
from django.utils import timezone

class ForeignStock(models.Model):
    ticker = models.CharField(max_length=4)
    name = models.CharField(max_length=30)
    dividend = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    amount = models.CharField(max_length=10)
    interest = models. CharField(max_length=3)

    def __str__(self):
        return self.ticker
