from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestCretaeCollection:
    def test_user(self):

        client= APIClient()
        response = client.get(
                path=reverse('article-list'),
                content_type='application/json',
                follow=True
            )    
        assert response.status_code==200