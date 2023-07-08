
#Django
from django.db.models.aggregates import Avg, Count

#Third party
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly,IsAuthenticated

#Local
from .models import Article
from .serilizers import ArticleSerializer



class ArticleViewSet(ModelViewSet):

    queryset = Article.objects.annotate(
    vote_number=Count('rates'),
    average=Avg('rates__rate')
    ).all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def get_serializer_context(self):
        return {'user_id':self.request.user.pk}
        # return {'user_id':self.request.user.id}