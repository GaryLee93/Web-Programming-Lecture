from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import News, Professor
# Create your views here.

def homepage(request):
    allNews = News.objects.all()
    return render(request,'homepage.html',locals())

def professor(request, slug):
    try:
        prof = Professor.objects.get(slug=slug)
        return render(request,'professor.html',locals())
    except:
        return redirect('/')

def member(request):
    profs = Professor.objects.all()
    return render(request,'member.html',locals())