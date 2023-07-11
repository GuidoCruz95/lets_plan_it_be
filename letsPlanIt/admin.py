from django.contrib import admin
from .models import Person, Subscription, Event, PaymentHistory


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['__all__']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ['__all__']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    fields = ['__all__']


@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    fields = ['__all__']
