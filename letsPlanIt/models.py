import uuid
from django.db import models


# class Macro(models.Model):
#     macro_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=20)
#     creation_date = models.CharField(max_length=100)
#     closing_date = models.CharField(max_length=100)
#
#
# class Cell(models.Model):
#     cell_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=20)
#     description = models.CharField(max_length=100)
#     macro = models.ForeignKey(Macro, on_delete=models.CASCADE, related_name='cells', null=True)

# TODO: Attributes that are to store dates, currently are defined as string, should be updated to date.

class Person(models.Model):
    ci = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthdate = models.CharField(max_length=30)
    about_you = models.CharField(max_length=200, default="")
    # cell = models.ForeignKey(Cell, on_delete=models.CASCADE, related_name='letsPlanIt', null=True)


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    cost = models.IntegerField()
    requirements = models.CharField(max_length=300)
    persons = models.ManyToManyField(Person, through='Subscription')


class Subscription(models.Model):
    subscription_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    notes = models.CharField(max_length=300)
    total_payed = models.IntegerField(default=0)


class PaymentHistory(models.Model):
    history_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=100)
    amount = models.IntegerField()
    notes = models.CharField(max_length=300)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
