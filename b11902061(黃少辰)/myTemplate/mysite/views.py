from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    msg = "Hello World"
    now = datetime.now()
    return render(request, "index.html", locals())

def index(request, tvno=0):
    tv_list = [{"name":"東森", "tvcode":"LuQ4S-i5zoE"},
               {'name':'民視', 'tvcode':'ylYJSBUgaMA'},
               {'name':'台視', 'tvcode':'xL0ch83RAK8'},
               {'name':'華視', 'tvcode':'wM0g8EoUZ_E'},
               {'name':'List', 'tvcode':'videoseries?list=RDCLAK5uy_mTDHYYJLCkFv8XL1Z8AFkMqF9RfQZzeRc'},
            ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, "index.html", locals())
