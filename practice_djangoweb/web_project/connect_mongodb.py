from pymongo import MongoClient
client=MongoClient('mongodb://172.17.0.3:27017/')
mydb=client.mydb
data={'title':'view mariaDB', 'tags':['db service']}
board_info=mydb.board.insert_one(data)
data=[{'name':'Ram', 'age':'26', 'city':'Hyderabad'},
{'name':'Rahim', 'age':'27', 'city':'Bangalore'}]
res=mydb.board.insert_many(data)
print('Data inserted ....', res.inserted_ids)
board_info=mydb.board.find()
for info in board_info:
    print(info)
client.close()



from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

#crawling=MongoClient('mongodb://172.17.0.3:27017/')
#mydb=crawling.mydb
#data={'title':'article infos', 'tags':['title link origin']}
#crawling_info=mydb.board.insert_one(data)

res=requests.get('http://media.daum.net/economic/')
if res.status_code==200:
    soup=BeautifulSoup(res.content,'html.parser')
    links=soup.find_all('a', class_='link_txt') # a tag 기준으로
    title=str()
    link=str()
    origins=soup.find_all('span', class_='info_thumb')

    origin=str()

    for link,origin in links, origins:
        title=str.strip(link.get_text())
        link=link.get('href')
        origin=str.strip(origins.get_text())
        print(origin)
        data=[{'title':title, 'link':link, 'origin':origin}]
        res=mydb.board.insert_many(data)
        print(res.inserted_ids)
        crawling_info=mydb.board.find()
        for info in crawling_info:
            print(info)

#crawling.close()




