from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup


res=requests.get('http://media.daum.net/economic/')
if res.status_code==200:
    soup=BeautifulSoup(res.content,'html.parser')
    links=soup.find_all('a', class_='link_txt') # a tag 기준으로
    title=str()
    link=str()
    origins=soup.find_all('span', class_='info_thumb')
    origins.append(soup.find_all('span', class_='info_mainnews'))
    origin=str()

    for link in links:
        title=str.strip(link.get_text())
        link=link.get('href')
        origins=origins.find_all('span', class_='info_thumb')
        origins.append()

        for origin in origins:
            print(origin)