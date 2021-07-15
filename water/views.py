from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def chart1(request):
    return render(request, 'chart1.html')

def chart2(request):
    return render(request, 'chart2.html')

def chart3(request):
    return render(request, 'chart3.html')

def ml(request):
    return render(request, 'ml.html')