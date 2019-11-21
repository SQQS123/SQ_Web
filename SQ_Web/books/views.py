from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Home.views import check_login
from Home.models import Users
from comics.models import Comics
from .forms import UploadPaintsForm
import os
import random

# windows
# BOOK_PATH_DIR = r"D:/books/"
# linux
BOOK_PATH_DIR = r"/mnt/books/"
BOOK_NAME_LST = []
for root, dirs, files in os.walk(BOOK_PATH_DIR):
    for file in files:
        BOOK_NAME_LST.append(file[:-4])


# 测试
def get_bookname(request):
    test = Comics.objects.get(bookname = "三字经")
    print(test.bookname)
    return HttpResponse("查找书名为xx的comics")


# 所有书籍名的菜单
def Books(request):
    context = {
        "book_name":BOOK_NAME_LST
    }
    return render(request, 'books/books.html', context)


@check_login
def get_user(request):
    return request.session['login_user']


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
        max_idx = len(Comics.objects.filter(bookname=book_name))
        if max_idx <= 1:
            idx = 0
        else:
            idx = random.randint(1, max_idx)
        try:
            paintsurl = Comics.objects.filter(bookname = book_name)[idx].get_paintsfile_url()
        except Exception as e:
            paintsurl = "/media/paints/default.jpg"
        context["paintsurl"] = paintsurl
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
        user = get_user(request)
        context = {
            "book_name": book_name,
            "user": user
        }
        form = UploadPaintsForm(request.POST, request.FILES)
        # 找到用户名的id
        form.instance.painter_id = Users.objects.get(username = user["username"]).id
        # form.instance.bookname = book_name

        print(user)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            page = form.cleaned_data['page']
            print(page)
            form.instance.page = page
            result = form.save()
            if result:
                print("True")
            return HttpResponse("提交成功")
        else:
            errors_obj = form.errors
            context["errors_obj"] = errors_obj
            # print("page_errors:",form.errors["page"])
            # print("paints_errors:", form.errors["paints"])
        # 应该返回一个提交成功的页面
        return HttpResponse("提交失败")
    # print(context['page'])
    return render(request, 'books/bookcontent.html', context)

