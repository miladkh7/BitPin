from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .factories import UserFactory,ArticleFactory
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

        sample_article = ArticleFactory()
        sample_article.author = cls.authenticated_user
        sample_article.save()
        cls.sample_article = sample_article


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


    def test_create_book_with_unauthenticated_user_by_token(self):
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
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def get_article(self):
        response = self.client.get(
            path=reverse('article-detail', kwargs={'pk': self.sample_article.pk}),
            content_type='application/json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.sample_article.title)
        self.assertEqual(response.data['content'], self.sample_article.content)
        self.assertEqual(response.data['author'], self.sample_article.author.username)

    def test_update_article_by_owner(self):
        self.client.login(
            username=self.authenticated_user.username,
            password='testp'
        )
        data = {
            "title": "test_title2",
            "content": "test_content2",
        }
        response = self.client.put(
            path=reverse('article-detail', kwargs={'pk': self.sample_article.pk}),
            data=data,
            content_type='application/json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])
    
    def test_update_article_by_not_owner(self):
        user = UserFactory()
        user.set_password('testp')
        user.save()
        self.client.login(
            username=user.username,
            password='testp'
        )
        data = {
            "title": "test_title2",
            "content": "test_content2",
        }
        response = self.client.put(
            path=reverse('article-detail', kwargs={'pk': self.sample_article.pk}),
            data=data,
            content_type='application/json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_article_by_owner(self):
        self.client.login(
            username=self.authenticated_user.username,
            password='testp'
        )
        response = self.client.delete(
            path=reverse('article-detail', kwargs={'pk': self.sample_article.pk}),
            content_type='application/json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)