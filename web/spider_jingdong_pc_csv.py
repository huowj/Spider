

"""
爬取京东笔记本型号价格
写csv啦啦啦
"""

import csv
import requests
import json
import re
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
        row=[]
        name=pc_li.find('div',attrs={'class':'p-name'}).find('em').getText()
        num_str=pc_li.find('div',attrs={'class':'p-img'}).find('a')['href']
        num=str(re.sub("\D","",num_str))
        url_p='https://p.3.cn/prices/mgets?skuIds=J_'+num
        html_p=requests.get(url_p).content
        price=json.loads(html_p)[0]['p']
        row.append(name)
        row.append(price)
        pc_name_list.append(row)
        
        #detail = pc_li.find('div', attrs={'class': 'p-name'}).find('a')
        #inner_url='https:'+detail['href']
        #inner_html=requests.get(inner_url, headers={
        #   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        #   }).content
        #inner_soup=BeautifulSoup(inner_html,"lxml")
        #pc_name = inner_soup.find('div', attrs={'class': 'itemInfo-wrap'}).find('div',attrs={'class':'sku-name'}).getText()
        #pc_name_list.append(pc_name)

    next_page = soup.find('span', attrs={'class': 'p-num'}).find('a',attrs={'class':'pn-next'})
    if next_page:
        return pc_name_list, DOWNLOAD_URL + next_page['href']
    return pc_name_list, None


def main():
    url = DOWNLOAD_URL

    with open('pcs.csv', 'w',newline='') as csvfile:
        header=['name','price']
        writer=csv.writer(csvfile)
        writer.writerow(header)
        while url:
            html = download_page(url)
            pcs, url = parse_html(html)
            writer.writerows(pcs)
            #fp.write(u'{pcs}\n'.format(pcs='\n'.join(pcs)))


if __name__ == '__main__':
    main()
