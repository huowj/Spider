

"""
什么鬼 豆瓣上的操作系统
我学操作系统容易么我
写csv啦啦啦
"""

import csv
import requests
import json
import re
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://book.douban.com'
url = DOWNLOAD_URL+'/subject_search?search_text=%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F&cat=1001'

def download_page(url):
    r=requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'})
    r.encoding='utf-8'
    return r.content


def parse_html(html):
    soup = BeautifulSoup(html,"lxml")
    book_list_soup = soup.find('ul', attrs={'class': 'subject-list'})

    book_name_list = []

    for book_li in book_list_soup.find_all('li',attrs={'class':'subject-item'}):
        row=[]
        name=book_li.find('div',attrs={'class':'info'}).find('a').getText()
        try:
            name_v=book_li.find('div',attrs={'class':'info'}).find('a').find('span').gettext()
        except:
            name_v=''
        finally:
            name_finally=name+name_v
        pub=book_li.find('div',attrs={'class':'pub'}).getText()
        try:
            star=book_li.find('div',
                              attrs={'star clearfix'}).find('span',
                                                            attrs={'rating_nums'}).getText()
        except:
            star=0
        
        #num_str=book_li.find('div',attrs={'class':'p-img'}).find('a')['href']
        #num=str(re.sub("\D","",num_str))
        #url_p='https://p.3.cn/prices/mgets?skuIds=J_'+num
        #html_p=requests.get(url_p).content
        #price=json.loads(html_p)[0]['p']
        row.append(name_finally)
        row.append(type(name_finally))
        row.append(pub)
        row.append(type(pub))
        row.append(star)
        row.append(type(star))
        book_name_list.append(row)
    print(book_name_list)
    print(type(name))
    print(type(pub))
    print(type(star))
    return book_name_list


html=download_page(url)
book=parse_html(html)
with open('book.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(book)
        #detail = book_li.find('div', attrs={'class': 'p-name'}).find('a')
        #inner_url='https:'+detail['href']
        #inner_html=requests.get(inner_url, headers={
        #   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        #   }).content
        #inner_soup=BeautifulSoup(inner_html,"lxml")
        #book_name = inner_soup.find('div', attrs={'class': 'itemInfo-wrap'}).find('div',attrs={'class':'sku-name'}).getText()
        #book_name_list.append(book_name)

##    next_page = soup.find('div', attrs={'class': 'paginator'}).find('span',attrs={'class':'next'}).find('a')
##    if next_page:
##        return book_name_list, DOWNLOAD_URL + next_page['href']
##    return book_name_list, None


##def main():
##    url = DOWNLOAD_URL+'/subject_search?search_text=%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F&cat=1001'
##
##    with open('books.csv', 'wb') as csvfile:
##        writer=csv.writer(csvfile)
##        while url:
##            html = download_page(url)
##            books, url = parse_html(html)
##            writer.writerows(books)
##            #file.write(u'{books}\n'.format(books='\n'.join(books)))
##
##
##if __name__ == '__main__':
##    main()
