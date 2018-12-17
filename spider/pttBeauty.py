import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import os
import sys
import json
import time
#目標頁面


for num in range(2000, 2751):
    res = requests.get('https://www.ptt.cc/bbs/Beauty/index2109.html')
    soup = BeautifulSoup(res.text, 'lxml')

    #使用迴圈進入到目標頁面中的每個主題頁面

    for article in soup.select('.r-ent a'):
        url = 'https://www.ptt.cc' + article['href']
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        #判斷網址中有沒有圖片，如果有就開始下載

        if len(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
            for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
                try:
                    #記得更改想要下載到的位
                    file_name = int(time.time())
                    urlretrieve(img_url['href'], os.path.dirname(os.path.abspath(__file__))+'/file/'+str(file_name)+'.jpg'.format(article.text, index))
                    new_dict = {"beauty": {}}
                    key = 0
                    try:
                        jsonFile = open(os.path.dirname(os.path.abspath(__file__))+"beauty.json","r")
                        fileContent = jsonFile.read()
                        new_dict = json.loads(fileContent)
                        key = len(new_dict['beauty'])
                        new_dict['beauty'].setdefault(key,str(file_name)+'.jpg')
                        key = key+1
                    except:
                        print ('error')

                    with open(os.path.dirname(os.path.abspath(__file__))+"beauty.json","w") as f:
                        json.dump(new_dict,f)
                        print("加载入文件完成...")
                except:
                    print('{} {}_{}.jpg 下載失敗!'.format(img_url['href'], article.text, index))
