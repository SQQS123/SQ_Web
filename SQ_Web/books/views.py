from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Books(request):
    return render(request, 'books/books.html')


# chapter menu
def chaptermenu(request,back_bookid):
    context = {
        "bookid":back_bookid
    }
    return render(request, 'books/chaptermenu.html', context)


# section menu
def sectionmenu(request,back_bookid,back_chapterid):
    context = {
        "bookid":back_bookid,
        "chapterid":back_chapterid
    }
    return render(request, 'books/sectionmenu.html', context)


# content
def content(request, back_bookid, back_chapterid, back_sectionid):
    context = {
        "bookid": back_bookid,
        "chapterid": back_chapterid,
        "sectionid": back_sectionid
    }
    return render(request, 'books/content.html', context)