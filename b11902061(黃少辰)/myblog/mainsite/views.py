from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Post, Music
from django.urls import reverse

# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
        return HttpResponse(html)
    except:
        return redirect('/')
    
def about(request, author_no=0):
    html = "<h2> This is No:" + str(author_no) + "\'s about page! </h2> <hr>"
    return HttpResponse(html)

def reverse_practice(request, year, month, day):
    html = "<h1> Date: {}-{}-{} </h1>".format(year, month, day)
    html += "<a href='{}'>Show the Post Link</a>".format(reverse('post-url', args=(year, month, day)))
    return HttpResponse(html)

def music_homepage(request):
    template = get_template('music_index.html')
    musics = Music.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def music(request, slug):
    template = get_template('music_post.html')
    try:
        music = Music.objects.get(slug=slug)
        if music != None:
            html = template.render(locals())
        return HttpResponse(html)
    except:
        return redirect('/music')
    
def form(request):
    verified = 1
    try:
        user_name = request.GET['user_name']
    except:
        user_name = None
        verified = -1
    try:
        age_check = request.GET['age_check']
    except:
        age_check = None
    try:
        math = request.GET["math"]
    except:
        math = None
    try:
        year = request.GET["year"]
    except:
        year = None
    try:
        num = request.GET.getlist('num')
    except:
        num = None
    try:
        message = request.GET["message"]
    except:
        message = None
    
    if verified == -1:
        return render(request, "form.html", locals())
    
    if user_name is None or age_check is None or num is None or message is None:
        verified = 0
    
    math_check = True
    if math != "3":
        verified = 0
        math_check = False
    
    num_check = True
    ans = ['0', '1', '2', '3', '5', '6', '7', '8', '9', '11', '12', '13', '14']
    if len(ans) == len(num):
        for i in range(len(num)):
            if num[i] != ans[i]:
                verified = 0
                num_check = False
                break
    else:
        verified = 0
        num_check = False
    
    year_check = True
    if year != "2024":
        verified = 0
        year_check = False
    
    years = range(1,10001)
    return render(request, "form.html", locals())