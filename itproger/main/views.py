from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def about_2(request):
    return render(request, 'main/about_2.html')

def about_3(request):
    return render(request, 'main/about_3.html')