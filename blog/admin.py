from django.contrib import admin

from .models import Article, Rate

admin.site.register(Article)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["article", "rate", "user"]
