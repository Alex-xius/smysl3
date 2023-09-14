from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home_page(request):
    articles = Article.objects.all()
    # использовал, чтобы обновить слаги
    # for article in articles:
    #     article.save()
    return render(request, 'blog/home_page.html', context={
        'articles': articles
        })

def article_page(request, slug_article):
    context = {'article': Article.objects.get(slug=slug_article)}
    return render(request, 'blog/article_page.html', context)