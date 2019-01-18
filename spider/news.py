from urllib.request import urlopen
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import os
import sys
import json
import time
import random


new_dict = {"news": {}}

html = urlopen('https://tw.appledaily.com/new/realtime/2')
bsObj = BeautifulSoup(html, "lxml")

news_list = bsObj.findAll("div", {"class":"item"})

for news in news_list:
    value = {}
    href = news.find('a')['href']
    img = news.find('img')
    title = img['alt']
    img_url = 'https:'+img['data-src']

    value['href'] = href
    value['title'] = title
    value['img_url'] = img_url

    try:
        # 記得更改想要下載到的位
        file_name = int(time.time())+random.randint(0,1000)
        urlretrieve(img_url, os.path.dirname(os.path.abspath(__file__))+'/file/'+str(file_name)+'.jpg')
        try:
            jsonFile = open(os.path.dirname(os.path.abspath(__file__))+"news.json","r")
            fileContent = jsonFile.read()
            new_dict = json.loads(fileContent)
            key = len(new_dict['news'])
            new_dict['news'].setdefault(key,value)
        except:
            print ('error')

        with open(os.path.dirname(os.path.abspath(__file__))+"news.json","w") as f:
            json.dump(new_dict,f)
            print("加载入文件完成...")
    except:
        print('{} {}_{}.jpg 下載失敗!')
