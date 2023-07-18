# Django
from django.db.models.aggregates import Avg, Count

# Third party
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.response import Response

# Local
from .models import Article
from .serilizers import ArticleSerializer, RateSerializer
from .pagination import DefaultPagination
from .permissions import IsAdminOrIsOwnerOrReadOnly

class ArticleViewSet(ModelViewSet):

    queryset = Article.objects.annotate(
        vote_number=Count("rates"), average=Avg("rates__rate")
    ).all()
    serializer_class = ArticleSerializer
    pagination_class = DefaultPagination
    permission_classes =[ IsAdminOrIsOwnerOrReadOnly, ]

    def get_serializer_context(self):
        return {"user_id": self.request.user.pk}
        # return {'user_id':self.request.user.id}

    @action(methods=["POST"], detail=True)
    def submit_rate(self, request, pk):
        article = self.get_object()
        serializer = RateSerializer(article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
