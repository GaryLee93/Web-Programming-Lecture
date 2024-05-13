from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .models import News
# Create your views here.

def homepage(request):
    allNews = News.objects.all()
    return render(request,'index.html',locals())
