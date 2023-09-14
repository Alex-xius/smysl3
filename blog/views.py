from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home_page(request):
    context = {'articles': Article.objects.all()}
    return render(request, 'blog/home_page.html', context)