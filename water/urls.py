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
from django.urls import path
from django.views.generic import TemplateView
from water import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('form', TemplateView.as_view(template_name='form-elements-component.html'), name='form'),
    path('table', TemplateView.as_view(template_name='bs-basic-table.html'), name='table'),
    path('map', TemplateView.as_view(template_name='map-google.html'), name='map'),
    path('sample', TemplateView.as_view(template_name='sample-page.html'), name='sample'),

    path('chart1', views.chart1, name='chart1'),
    path('chart2', views.chart2, name='chart2'),
    path('chart3', views.chart3, name='chart3'),
    path('ml', views.ml, name='ml'),
]
