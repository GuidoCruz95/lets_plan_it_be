from rest_framework import serializers
from letsPlanIt.models import Person, Event, Subscription, PaymentHistory


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['ci', 'email', 'name', 'lastname', 'birthdate', 'about_you']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date', 'location', 'cost', 'requirements']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['notes', 'total_payed', 'person', 'event', 'total_payed']


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = ['date', 'amount', 'notes', 'subscription']
