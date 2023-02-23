from rest_framework import viewsets
from church.serializers import PersonSerializer, EventSerializer
from church.models import Person, Event


# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
