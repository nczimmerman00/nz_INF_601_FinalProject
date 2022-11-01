from django.db import models


# Create your models here.
class Articles(models.Model):
    article_title = models.CharField(max_length=75)
    pub_date = models.DateTimeField('date published')
    article_author = models.CharField(max_length=50)
    article_text = models.CharField(max_length=1000)
    article_category = models.CharField(max_length=25)
