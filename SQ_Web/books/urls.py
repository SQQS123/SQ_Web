from django.urls import path
from . import views

app_name = 'Book'

urlpatterns = [
 # book list

 path('', views.Books, name='books'),
 path('find/', views.get_bookname, name='findbooks'),
 # chapter menu
 path("<str:book_name>/", views.bookmenu, name="book_name"),

 # section menu
 # path("book_<int:back_bookid>/chapter_<int:back_chapterid>/",
 #      views.sectionmenu, name="sectionmenu"),
 # section content
 # path("book_<int:back_bookid>/chapter_<int:back_chapterid>/section_<int:back_sectionid>/",
 #      views.content, name="content")
]