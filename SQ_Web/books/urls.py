from django.urls import path
from . import views


urlpatterns = [
 # book list
 path('', views.Books, name='books'),
 # chapter menu
 path("book_<int:back_bookid>/", views.chaptermenu, name="chaptermenu"),
 # section menu
 path("book_<int:back_bookid>/chapter_<int:back_chapterid>/",
      views.sectionmenu, name="sectionmenu"),
 # section content
 path("book_<int:back_bookid>/chapter_<int:back_chapterid>/section_<int:back_sectionid>/",
      views.content, name="content")
]