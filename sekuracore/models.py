import string
import random
from django.db import models


def random_string(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(chars, k=length))


def random_string_100():
    return random_string(100)


class Agent(models.Model):
    DISABLED = "D"
    APPROVED = "A"
    REJECTED = "R"
    STATUS_CHOICES = [
        (DISABLED, "Disabled"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected"),
    ]

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=1, default=DISABLED, choices=STATUS_CHOICES)
    source_of_truth = models.BooleanField(default=False)
    secret = models.BinaryField(blank=True, null=True)
    parameters = models.CharField(max_length=200, blank=True, null=True, help_text="Comma-separated fields")

    class Meta:
        indexes = [
            models.Index(fields=["name", "secret"]),
        ]

    def __str__(self):
        return self.name


class Employee(models.Model):
    ONBOARDING = "O"
    ACTIVE = "A"
    OFFBOARDING = "D"
    OFFBOARDED = "R"
    STATUS_CHOICES = [
        (ONBOARDING, "Onboarding"),
        (ACTIVE, "Active"),
        (OFFBOARDING, "Offboarding"),
        (OFFBOARDED, "Offboarded"),
    ]
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=ONBOARDING)

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        return f"{self.name} {self.lastname} <{self.email}>"


class Access(models.Model):
    ACTIVE = "A"
    DISABLED = "D"
    REVOKED = "R"
    STATUS_CHOICES = [
        (DISABLED, "Disabled"),
        (ACTIVE, "Active"),
        (REVOKED, "Revoked"),
    ]
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, related_name="access")
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE, related_name="access")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=DISABLED)
    data = models.TextField()

    class Meta:
        verbose_name_plural = "accesses"
        indexes = [
            models.Index(fields=["agent"]),
            models.Index(fields=["employee"]),
        ]

    def __str__(self):
        return f"{self.agent} {self.employee} <{self.email}>"
