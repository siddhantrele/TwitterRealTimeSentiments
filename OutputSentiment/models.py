from django.db import models

from django.utils import timezone
import datetime

class Tweet(models.Model):
    term = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    sentiment = models.FloatField()
    created_date = models.DateTimeField(
            default=datetime.datetime.now)
