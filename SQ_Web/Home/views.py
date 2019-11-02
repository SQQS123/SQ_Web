from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'Home/Home.html')


def Hello(request):
    return HttpResponse("Hello world")