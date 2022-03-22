from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'diabetes/index.html')

def about(request):
    return render(request, 'diabetes/about.html')

def blog(request):
    return render(request, 'diabetes/blog.html')

def analyze(request):
    return render(request,'diabetes/analyze.html')
