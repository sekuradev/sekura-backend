from django.shortcuts import render
from rest_framework import generics

from . import models, serializers


def index(request):
    return render(request, "index.html")


class Agent(generics.RetrieveAPIView):
    queryset = models.Agent.objects.all()
    serializer_class = serializers.Agent


class Employee(generics.RetrieveAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.Employee


class Access(generics.RetrieveAPIView):
    queryset = models.Access.objects.all()
    serializer_class = serializers.Access
