from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Home.views import check_login
from .forms import UploadPaintsForm
import os


BOOK_PATH_DIR = r"D:/books/"
BOOK_NAME_LST = []
for root, dirs, files in os.walk(BOOK_PATH_DIR):
    for file in files:
        BOOK_NAME_LST.append(file[:-4])


# 所有书籍名的菜单
def Books(request):
    context = {
        "book_name":BOOK_NAME_LST
    }
    return render(request, 'books/books.html', context)


@check_login
def upload_file(form):
    pass


def split_article_content(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        book_contents = f.readlines()
    i = 0
    j = 0
    section_cnt = []
    while i < len(book_contents) - 3:
        if i == 0:
            section_cnt.append(book_contents[i])
            i = i + 1
            continue
        elif book_contents[i] == '\n' and book_contents[i + 1] == '\n' and book_contents[i + 2] == '\n' and \
                book_contents[i + 3] != '\n':
            section_cnt.append(book_contents[i + 3])
            i = i + 4
            j = j + 1
            continue
        section_cnt[j] += book_contents[i]
        i = i + 1
    return section_cnt


# 每本书里的菜单
def bookmenu(request,book_name):

    filename = BOOK_PATH_DIR + book_name + '.txt'
    # 这里我想使用上拉加载更多的功能
    # 下面实现了分页功能
    context = {
        "book_name": book_name,
    }
    if request.method == 'GET':
        section_cnt = split_article_content(filename)
        paginator = Paginator(section_cnt, 1)
        # paginator.page_range -> range(1, xxx)
        try:
            page = int(request.GET['page'])
            book_content = paginator.page(page)
            context["page"] = page
            context["book_content"] = book_content
        except Exception as e:
            book_content = paginator.page(1)
            page = 1
            context["page"] = page
            context["book_content"] = book_content

    if request.method == 'POST':
        context = {
            "book_name": book_name,
        }
        form = UploadPaintsForm(request.POST, request.FILES)
        print(form.is_valid())
        # print(request.POST,request.FILES)
        # print(request.POST["paintsfile"])
        if form.is_valid():
            result = form.save()
            if result:
                print("True")
            page = form.cleaned_data['page']
            print(page)
        else:
            errors_obj = form.errors
            context["errors_obj"] = errors_obj
            # print("page_errors:",form.errors["page"])
            print("paints_errors:", form.errors["paints"])
    # print(context['page'])
    return render(request, 'books/bookcontent.html', context)

