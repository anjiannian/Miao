# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pub_page/index.html')

def intro(request):
    return render(request, 'pub_page/intro.html')
#
#def content_lists(request):
#    return
#
#def content(request):
#    return
#
#def volunteer(request):
#    return

