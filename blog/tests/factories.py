import random

from django.contrib.auth import get_user_model

import factory
from factory.django import DjangoModelFactory
from factory import Faker

factory.Faker._DEFAULT_LOCALE = 'en_US'

class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    name = Faker('name')
    username= Faker('user_name')
