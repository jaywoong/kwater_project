"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard1', views.dashboard1, name='dashboard1'),
    path('dashboard2', views.dashboard2, name='dashboard2'),
    path('dashboard3', views.dashboard3, name='dashboard3'),
    path('dashboard4', views.dashboard3, name='dashboard4'),
    path('dashboard5', views.dashboard3, name='dashboard5'),
    path('dashboard6', views.dashboard3, name='dashboard6'),
    path('dashboard7', views.dashboard3, name='dashboard7'),
    path('dashboard8', views.dashboard3, name='dashboard8'),
    path('dashboard9', views.dashboard3, name='dashboard9'),
    path('dashboard10', views.dashboard3, name='dashboard10'),
    path('dashboard11', views.dashboard3, name='dashboard11'),
]
