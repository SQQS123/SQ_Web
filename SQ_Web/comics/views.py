from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Comics(request):
    return render(request, 'comics/comics.html')