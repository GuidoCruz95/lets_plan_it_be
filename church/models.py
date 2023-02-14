from django.db import models
import datetime


# Create your models here.
class Person(models.Model):
    ci = models.IntegerField()
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthdate = models.CharField(max_length=30)
