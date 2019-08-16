from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Библиотека для поиска запросов по несольким полям
from django.db.models import Q

# Create your views here.
def index(request):
    slider_first = Slider_first.objects.all()
    slider = Slider.objects.all()

    # поиск
    search_query = request.GET.get('search', '')
    if search_query:
        blog = Blog.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))
    else:
        blog = Blog.objects.all()


    context = {'slider_first': slider_first,
               'slider': slider,
               'blog': blog}

    return render(request, 'photobloger/index.html', context)


def detail_blog(request, slug):
    blogs = Blog.objects.get(slug__iexact=slug)
    context = {'blogs': blogs}
    return render(request, 'photobloger/details.html', context)

def acount(request):
    name = 'misha'
    return render(request, 'photobloger/acount.html', {'name': name})
