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
        fields = ['id', 'title', 'average',
                  'vote_number', 'content', 'user_vote']

    average = serializers.FloatField(read_only=True)
    vote_number = serializers.IntegerField(read_only=True)
    user_vote = serializers.SerializerMethodField()

    def get_user_vote(self, obj: Article):
        user_id = self.context['user_id']
        rate = obj.rates.filter(user_id=user_id).first()
        if rate:
            return rate.rate
        return None

    def create(self, validated_data):
        user_id = self.context['user_id']
        user = get_object_or_404(get_user_model(), pk=user_id)
        return Article.objects.create(author=user, **validated_data)
    

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['rate']

    def create(self, validated_data):
        user_id = self.context['user_id']
        user = get_object_or_404(get_user_model(), pk=user_id)
        return Rate.objects.create(author=user, **validated_data)