import datetime

from django.db import models
from django.utils import timezone

class Guestbook(models.Model):
    name = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=32)
    pub_date = models.DateTimeField('date published')

class Subscriber(models.Model):
    email = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date inserted')
