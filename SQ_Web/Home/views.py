from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Home/Home.html')


def Hello(request):
    return HttpResponse("Hello world")