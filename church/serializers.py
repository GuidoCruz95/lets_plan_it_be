from rest_framework import serializers
from church.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['ci', 'email', 'name', 'lastname', 'birthdate']
