from django.shortcuts import render
from django.http import HttpResponse
from Home.views import check_login


# Create your views here.
def Comics(request):
    return render(request, 'comics/comics.html')


@check_login
def Submit_paint(request):
    if request.method == 'GET':
        print(request.GET)
    return HttpResponse("提交作品")