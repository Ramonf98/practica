from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


class PersonView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Person.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)