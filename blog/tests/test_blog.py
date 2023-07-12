from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .factories import UserFactory
class BlogTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.client = APIClient()
        user_authenticated =UserFactory()
        user_authenticated.set_password('testp')
        user_authenticated.save()
        cls.authenticated_user= user_authenticated

    def setUp(self) -> None:
        
        return super().setUp()

    def test_get_blog_posts(self):
            response = self.client.get(
                path=reverse('article-list'),
                content_type='application/json',
                follow=True
            ) 
            self.assertEqual(response.status_code, status.HTTP_200_OK)
