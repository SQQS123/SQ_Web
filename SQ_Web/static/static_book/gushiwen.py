from urllib import request
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) App' 
                       'leWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
}

booklist_url = "https://so.gushiwen.org/guwen/book_"
base_url = "https://so.gushiwen.org"
url_suffix = '.aspx'


def get_book(url):
    req = request.Request(url, headers=header)
    html = request.urlopen(req).read()
    etree_html = etree.HTML(html)
    # 书名
    title = etree_html.xpath('//h1/span/b//text()')
    # print(title[0])
    filename = title[0] + '.txt'
    # 找到书每个章节对应的网址
    # 每个章节的标题
    chapter_title = etree_html.xpath('//div[@class="bookcont"]//a//text()')
    print(chapter_title)

    file = open(filename, 'a', encoding='utf-8')
    bookcont_url = etree_html.xpath('//div[@class="bookcont"]//a/@href')

    k = 0
    # 然后开始从每个章节的网址中爬取内容
    for i in bookcont_url:
        chapter_url = base_url + i
        req = request.Request(chapter_url, headers=header)
        html = request.urlopen(req).read()
        HTML = html.decode("UTF-8")
        etree_html = etree.HTML(HTML)
        file.write('\u3000\u3000' + chapter_title[k])
        k += 1
        content = etree_html.xpath('//div[@class="contson"]//text()')
        for j in content:
            file.write(j + '\n')
        file.write('\n\n')
        # print(content)


if __name__ == "__main__":
    i = 334       #目前一共334本书
    while i < 335:
        bookcont_url = booklist_url + str(i) + url_suffix
        # print(bookcont_url)
        get_book(bookcont_url)
        i += 1



    # contson = etree_html.xpath('//div[@class="contson"]//text()')
    # result = html.decode("UTF-8")
    # print(bookcont_url)