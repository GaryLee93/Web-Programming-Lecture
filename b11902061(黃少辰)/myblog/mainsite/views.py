from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post
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