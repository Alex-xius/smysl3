from django.db import models
from pytils.translit import slugify
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    full_text = models.TextField()
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    slug = models.SlugField(default='', null=False)

    #Обноваляет слаги
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('article-detail', args=[self.slug])
    
    def __str__(self) -> str:
        return self.title
