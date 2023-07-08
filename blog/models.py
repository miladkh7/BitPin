#Django
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Title')
    content = models.TextField(null=True)
    
    def __str__(self) -> str:
        return f"{self.author}-{self.title}"