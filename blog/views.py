from rest_framework.viewsets import ModelViewSet
from django.db.models.aggregates import Avg, Count
from .serilizers import ArticleSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import Article
# Create your views here.


class ArticleViewSet(ModelViewSet):
    
    queryset = Article.objects.annotate(
    vote_number=Count('rates'),
    average=Avg('rates__rate')
    ).all()
    serializer_class = ArticleSerializer