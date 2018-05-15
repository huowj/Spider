import codecs
import requests
from bs4 import BeautifulSoup
DOWNLOAD_URL = 'http://www.hanteo.com/rank/nchart2.asp?Page=daily&genre=9'
url=DOWNLOAD_URL
html=requests.get(url,headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content
soup = BeautifulSoup(html,"lxml")
print(soup)

