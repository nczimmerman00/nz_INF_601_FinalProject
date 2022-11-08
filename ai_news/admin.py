from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['article_title', 'article_slug']


admin.site.register(Article, ArticleAdmin)
