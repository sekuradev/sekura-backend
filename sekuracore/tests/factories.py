import factory
from django.conf import settings
from sekuracore import models
from django.contrib.auth import get_user_model

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        abstract = False
        model = get_user_model()

    username = factory.Faker("user_name")
    email = factory.Faker("email")

    is_superuser = False
    is_staff = False
    is_active = True

