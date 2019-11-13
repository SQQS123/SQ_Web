from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def personal(request):
    return HttpResponse("personal")