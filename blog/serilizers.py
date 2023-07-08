from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title','average','vote_number','content']

    average = serializers.FloatField(read_only=True)
    vote_number = serializers.IntegerField(read_only=True)
        