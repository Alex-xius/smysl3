from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    full_text = models.TextField()
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
