import csv
import requests
import json
import re
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://list.jd.com/list.html?cat=670,671,672'

url=DOWNLOAD_URL
html=requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

soup = BeautifulSoup(html,"lxml")
pc_list_soup = soup.find('ul', attrs={'class': 'gl-warp clearfix '})
pc_name_list = []
pc_li=pc_list_soup.find_all('li',attrs={'class':'gl-item'})[43]
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
print(pc_name_list)
