from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Professor
# Create your views here.

def homepage(request):
    allNews = News.objects.all()
    return render(request,'homepage.html',locals())

def professor(request, num):
    prof = Professor.objects.all()[num]
    return render(request,'professor.html',locals())
