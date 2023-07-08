# Django
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="Title")
    content = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.author}-{self.title}"


class Rate(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="rates")
    rate = models.PositiveSmallIntegerField(
        default=2, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = [["article", "user"]]

    def __str__(self) -> str:
        return f"article : {self.article} - rate : {self.rate} - user : {self.user}"
