#Django
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# 3third party
from rest_framework import serializers

#local
from .models import Article, Rate

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title','average','vote_number','content']

    average = serializers.FloatField(read_only=True)
    vote_number = serializers.IntegerField(read_only=True)
        

    def create(self, validated_data):
        user_id = self.context['user_id']
        user = get_object_or_404(get_user_model(), pk=user_id)
        return Article.objects.create(author=user, **validated_data)
    

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        field = ['article', 'rate']

    def create(self, validated_data):
        user_id = self.context['user_id']
        user = get_object_or_404(get_user_model(), pk=user_id)
        return Rate.objects.create(author=user, **validated_data)
