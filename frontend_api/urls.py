"""DBlocks_Frontend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from frontend_api import get_wrapper,post_wrapper
from frontend_api import views
urlpatterns = [
    path('get_wrapper',get_wrapper.get_wrapper,name='get_wrapper'),
    path('post_wrapper',post_wrapper.post_wrapper,name='get_wrapper'),
    path('homepage',views.HomePage,name='homepage'),
    path('posts',views.posts,name='posts'),
    path('posts/<slug:slug>',views.post_details,name='post_details'),

]
