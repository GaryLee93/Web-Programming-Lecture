from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from .models import Post
import os


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

def video_play(request,tvno=0):
    if(request.path.find('/liked_song/') != -1):
        videoType = 0
        tv_list = [{'name':'Sci-Fi ROMANCE TRAVELER','tvcode':'VkRi59oa5Eg?si=3148n5xYkarc1yih'},
                {'name':'ダイナマイト','tvcode':'3GUx7x2Ko3s?si=1QoU9aSQtievONg-'},
                {'name':'無意識レクイエム (cosmobsp rmx) ','tvcode':'hCgAiV-MYYw?si=ZV-zckkGlYXtIJWc'},
                {'name':'空想メソロギヰ','tvcode':'ZZvJY7_gyfw?si=jBJJYTmY1GHREoO8'}]
    elif(request.path.find('/tv/') != -1):
        videoType = 1
        tv_list = [{'name':'NASA','tvcode':'21X5lGlDOfg?si=mUrpRySBg4Tu5MSU'},
                {'name':'campFire','tvcode':'mKCieTImjvU?si=DJEZEjM9WrVmuBiL'}]
    tvno = tvno
    tv = tv_list[tvno]
    now = datetime.now()
    return render(request,'tv.html',locals())

def carlist(request,maker=0):
    car_maker = ['Ford','Honda','Mozada']
    car_list = [[{'model':'Mustang','price':900000},
                {'model':'Fiesta','price':203500},
                {'model':'Focus','price':605000}],
                [{'model':'Fit','price':450000},
                {'model':'City','price':150000},
                {'model':'NSX','price':1200000}],
                [{'model':'Mazada3','price':329999},
                {'model':'Mazada5','price':603000},
                {'model':'Mazada6','price':850000}]]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request,'carlist.html',locals())