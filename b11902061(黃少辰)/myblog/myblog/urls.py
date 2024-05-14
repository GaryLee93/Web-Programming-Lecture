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
from django.contrib import admin
from django.urls import path
from mainsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage),
    path('post/<slug:slug>/', views.showpost),
    path('about/', views.about),
    path('about/<int:author_no>', views.about),
    path('date/<int:year>/<int:month>/<int:day>', views.reverse_practice, name='post-url'),
    path("music/", views.music_homepage),
    path("music/<slug:slug>", views.music),
]
