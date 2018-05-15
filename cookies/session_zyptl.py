import requests
from bs4 import BeautifulSoup

url="http://www.v2ex.com/signin"
UA="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"

header={"User-Agent":UA}

v2ex_session=requests.Session()
print(v2ex_session)
f=v2ex_session.get(url,headers=header)
print(f)

soup=BeautifulSoup(f.content,"html.parser")
print(soup)

once=soup.find('input',{'name':'once'})['value']
print(once)

name=soup.find('form',{'action':'/signin'}).find('input',{'type':'text'})['name']
print(name)

pw=soup.find('form',{'action':'/signin'}).find('input',{'type':'password'})['name']
print(pw)
print(type(pw))

postData={name:'1103983230@qq.com',
          pw:'jaychou1324',
          'once':once,
          'next':'/'
          }

v2ex_session.post(url,data=postData,headers=header)
print(v2ex_session)

f=v2ex_session.get('https://www.v2ex.com/settings',headers=header)
print(f.content.decode())

