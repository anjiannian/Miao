# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pub_page/index.html')

def intro(request):
    return render(request, 'pub_page/intro.html')
def news(request):
    return render(request, 'pub_page/news.html')
def articles(request):
    return render(request, 'pub_page/articles.html')

def feelings(request):
    return render(request, 'pub_page/feelings.html')
def train_classes(request):
    return render(request, 'pub_page/train_classes.html')


#
#def content_lists(request):
#    return
#
#def content(request):
#    return
#
#def volunteer(request):
#    return

