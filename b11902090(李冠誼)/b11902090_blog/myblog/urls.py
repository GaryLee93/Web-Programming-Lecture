"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from mainsite import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homepage),
    path('post/<slug:slug>/',views.showpost),
    path('about/',views.about),
    path('about/<int:author_no>',views.about),
    path('list',views.listing),
    path('form',views.show_post),
    path('<int:pid>/<str:del_pass>',views.show_post),
    path('tv/',views.video_play,name='tv-url'),
    path('tv/<int:tvno>/',views.video_play,name='tv-url'),
    path('liked_song/',views.video_play,name='liked_song'),
    path('liked_song/<int:tvno>',views.video_play,name='liked_song'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
