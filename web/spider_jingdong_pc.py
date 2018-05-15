#!/usr/bin/env python
# encoding=utf-8

"""
爬取京东笔记本型号价格
"""

import codecs

import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://list.jd.com/list.html?cat=670,671,672'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html,"lxml")
    pc_list_soup = soup.find('ul', attrs={'class': 'gl-warp clearfix '})

    pc_name_list = []

    for pc_li in pc_list_soup.find_all('li',attrs={'class':'gl-item'}):
        detail = pc_li.find('div', attrs={'class': 'p-name'}).find('a')
        inner_url='https:'+detail['href']
        inner_html=requests.get(inner_url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            }).content
        inner_soup=BeautifulSoup(inner_html,"lxml")
        pc_name = str.lstrip(inner_soup.find('div', attrs={'class': 'itemInfo-wrap'}).find('div',attrs={'class':'sku-name'}).getText())
        pc_name_list.append(pc_name)

    next_page = soup.find('span', attrs={'class': 'p-num'}).find('a',attrs={'class':'pn-next'})
    if next_page:
        return pc_name_list, DOWNLOAD_URL + next_page['href']
    return pc_name_list, None


def main():
    url = DOWNLOAD_URL

    with codecs.open('pcs', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            pcs, url = parse_html(html)
            fp.write(u'{pcs}\n'.format(pcs='\n'.join(pcs)))


if __name__ == '__main__':
    main()
