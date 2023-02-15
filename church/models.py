import uuid

from django.db import models


class Macro(models.Model):
    macro_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    creation_date = models.CharField(max_length=100)
    closing_date = models.CharField(max_length=100)


class Cell(models.Model):
    cell_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    macro = models.ForeignKey(Macro, on_delete=models.CASCADE, related_name='cells', null=True)


class Person(models.Model):
    ci = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthdate = models.CharField(max_length=30)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE, related_name='people', null=True)
