import json
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'section':'main_section.html',
    };
    return render(request, 'index.html',context);

def dashboard1(request):
    context = {
        'section':'dashboard1.html',
    };
    return render(request, 'index.html',context);

def dashboard2(request):
    context = {
        'section':'dashboard2.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard3.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard4.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard5.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard6.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard7.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard8.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard9.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard10.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard11.html',
    };
    return render(request, 'index.html',context);