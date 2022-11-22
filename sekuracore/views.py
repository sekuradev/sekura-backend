from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


def index(request):
    return render(request, "index.html")


class Agent(generics.ListAPIView):
    queryset = models.Agent.objects.all()
    serializer_class = serializers.Agent
    permission_classes = (IsAuthenticated,)


class AgentRegister(generics.CreateAPIView):
    serializer_class = serializers.AgentRegister

    def create(request, *args, **kwargs):
        return Response({})


class Employee(generics.RetrieveAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.Employee


class Access(generics.RetrieveAPIView):
    queryset = models.Access.objects.all()
    serializer_class = serializers.Access
