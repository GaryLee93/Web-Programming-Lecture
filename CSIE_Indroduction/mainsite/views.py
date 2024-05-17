from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from mainsite import models
# Create your views here.

def homepage(request):
    allNews = models.News.objects.all()
    return render(request,'homepage.html',locals())

def professor(request, slug):
    try:
        prof = models.Professor.objects.get(slug=slug)
        return render(request,'professor.html',locals())
    except:
        return redirect('/')

def professorIndex(request):
    profs = models.Professor.objects.all()
    return render(request,'professor_index.html',locals())

def courseIndex(request):
    courses = models.course.objects.all()
    return render(request,'course_index.html',locals())

def facilityIndex(request):
    facilities = models.facility.objects.all()
    return render(request,'facility_index.html',locals())
