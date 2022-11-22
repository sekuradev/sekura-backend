from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


class User(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ["password"]
        depth = 0


class Agent(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = "__all__"
        depth = 0


class AgentRegister(serializers.ModelSerializer):
    preshared_secret = serializers.CharField(max_length=500)

    class Meta:
        model = models.Agent


class Employee(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"
        depth = 0


class Access(serializers.ModelSerializer):
    class Meta:
        model = models.Access
        fields = "__all__"
        depth = 1
