from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from .models import Post

# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals()) #locals() return all local variabel on memory
    return HttpResponse(html)

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def about(request,author_no=0):
    html = "<h2>Here is No:{}'s about page<h2>".format(author_no)
    return HttpResponse(html)

def post(request,yr,mon,day,postnum):
    html = "<h2>date is {}/{}/{}!! Your post num is {}<h2>".format(yr,mon,day,postnum)
    return HttpResponse(html)

def post2(request,yr,mon,day):
    return render(request,'post2.html',locals())

def template_test(request,tvno=0):
    tv_list = [{'name':'NASA','tvcode':'21X5lGlDOfg?si=mUrpRySBg4Tu5MSU'},
               {'name':'campFire','tvcode':'mKCieTImjvU?si=DJEZEjM9WrVmuBiL'}]
    tvno = tvno
    tv = tv_list[tvno]
    now = datetime.now()
    return render(request,'template_test.html',locals())