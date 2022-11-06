from django.db import models


# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    article_author = models.CharField(max_length=50)
    article_text = models.CharField(max_length=3000)
    article_category = models.CharField(max_length=25)
