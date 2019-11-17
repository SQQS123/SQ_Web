from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


# 每本书里的菜单
def bookmenu(request,book_name):

    filename = BOOK_PATH_DIR + book_name + '.txt'
    # 这里我想使用上拉加载更多的功能
    # 下面实现了分页功能
    if request.method == 'GET':
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
            elif book_contents[i] == '\n' and book_contents[i + 1] == '\n' and book_contents[i + 2] == '\n' and book_contents[i + 3] != '\n':
                section_cnt.append(book_contents[i + 3])
                i = i + 4
                j = j + 1
                continue
            section_cnt[j] += book_contents[i]
            i = i + 1

        paginator = Paginator(section_cnt, 1)
        # paginator.page_range -> range(1, xxx)
        try:
            page = int(request.GET['page'])
            book_content = paginator.page(page)
        except Exception as e:
            book_content = paginator.page(1)
    context = {
        "book_name": book_name,
        "book_content":book_content,

    }
    return render(request, 'books/bookcontent.html', context)

