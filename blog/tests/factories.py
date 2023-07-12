import random

from django.contrib.auth import get_user_model

import factory
from factory.django import DjangoModelFactory
from factory import Faker

from ..models import Article
factory.Faker._DEFAULT_LOCALE = 'en_US'

class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    name = Faker('name')
    username= Faker('user_name')


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    author = factory.SubFactory(UserFactory)
    content = factory.Faker('text')
    title = factory.Sequence(lambda n: 'post%d' % n)