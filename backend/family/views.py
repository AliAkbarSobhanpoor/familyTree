# views.py
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonListAPIView(generics.ListAPIView):
    """
    Returns a list of all people with relationships.
    """
    queryset = Person.objects.prefetch_related('spouses', 'parents', 'children_of').all()
    serializer_class = PersonSerializer
    