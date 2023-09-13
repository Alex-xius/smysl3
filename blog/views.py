from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('''<html><title>Сайт Алексея Исаева</title>
                        <h1>Алексей Исаев</h1></html>''')