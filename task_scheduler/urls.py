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
from django.urls import path,include
from .views import CreateTeam
from .views import CreateTask
from .views import UpdateTask
from .views import GetAllTasksApi

urlpatterns = [
    path('create-team',CreateTeam.as_view(),name='create_team'),
    path('create-task',CreateTask.as_view(),name='create_task'),
    path('update-task/<int:pk>',UpdateTask.as_view(),name='update_task'),
    path('all-tasks',GetAllTasksApi.as_view(),name='all_tasks')
]