from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .factories import UserFactory
from ..models import Article
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

    def test_create_book_with_authenticated_user(self):
        self.client.login(
            username=self.authenticated_user.username,
            password='testp'
        )
        data = {
            "title": "test_title",
            "content": "test_content",
        }
        response = self.client.post(
            path=reverse('article-list'),
            data=data,
            content_type='application/json',
            follow=True
        )

        # check response code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # verify data created
        self.assertTrue(Article.objects.filter(title="test_title").exists())
        self.assertEqual(Article.objects.filter(title="test_title").get().author, self.authenticated_user)
        self.assertEqual(Article.objects.filter(title="test_title").get().content, data['content'])