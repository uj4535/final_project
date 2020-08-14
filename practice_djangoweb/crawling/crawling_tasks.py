from background_task import background
import time
import requests
from bs4 import BeautifulSoup
import sqlite3

@background()  # per second
def task_crawling_daum(schedule=2, repeat=60*3):
    conn=sqlite3.connect('db.sqlite3')
    conn.commit()
    conn.close
    res=requests.get('http://media.daum.net/economic/')
    if res.status_code==200:
        soup=BeautifulSoup(res.content,'html.parser')
        links=soup.find_all('a', class_='link_txt') # a tag 기준으로
        with sqlite3.connect('db.sqlite3') as con:
            cur=con.cursor()
            title=str()
            link=str()
            for link in links:
                title=str.strip(link.get_text())
                link=link.get('href')
                cur.execute("INSERT INTO economic (title, link) VALUES (?,?)",(title, link))
            con.commit()
        print('task_crawling_daum:', type(links), len(links))            
    time_tuple=time.localtime()
    time_str=time.strftime("%m%d%Y, %H:%M:%S", time_tuple)
    print("task_crawling_daum: !", type(links), len(links), time_str)

@background()
def task_hello(schedule=10, repeat=60):
    time_tuple=time.localtime()
    time_str=time.strftime("%m%d%Y, %H:%M:%S", time_tuple)
    print("task... Hello world!", time_str)