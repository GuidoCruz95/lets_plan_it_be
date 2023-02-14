from rest_framework import viewsets
from church.serializers import PersonSerializer
from church.models import Person


# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
