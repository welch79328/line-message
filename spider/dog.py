# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time
import sys
import json
import time




list_url = []
for num in range(1,100):

    url = 'http://www.tooopen.com/img/89_321_1_%s.aspx' % (num)
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    req = requests.get(url = url,headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    targets_url = bf.find_all(class_='pic')

    for each in targets_url:
        s=each.img.get('alt')
        t='狗'
        t2 = '犬'
        result = t in s
        result2 = t2 in s
        if result or result2 :
            list_url.append(each.img.get('alt') + '=' + each.get('href'))

print('连接采集完成')

print (list_url)

for each_img in list_url:
    try:
        file_name = int(time.time())
        img_info = each_img.split('=')
        target_url = img_info[1]
        filename = img_info[0] + '.jpg'
        print('下载：' + filename)
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        img_req = requests.get(url = target_url,headers = headers)
        img_req.encoding = 'utf-8'
        img_html = img_req.text
        img_bf_1 = BeautifulSoup(img_html, 'lxml')
        img_url = img_bf_1.find_all('div', class_='sc-det c-fix')
        img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
        img_url = img_bf_2.div.img.get('src')
        print (img_url )
        #if 'images' not in os.listdir():
        #    os.makedirs('images')

        urlretrieve(url = img_url,filename = os.path.dirname(os.path.abspath(__file__))+'/dogfile/' + str(file_name) + '.jpg')
        new_dict = {"dog": {}}
        key = 0
        try:
            jsonFile = open(os.path.dirname(os.path.abspath(__file__))+"dog.json","r")
            fileContent = jsonFile.read()
            new_dict = json.loads(fileContent)
            key = len(new_dict['dog'])
            new_dict['dog'].setdefault(key,str(file_name)+'.jpg')
            key = key+1
        except:
            print ('error')

        with open(os.path.dirname(os.path.abspath(__file__))+"dog.json","w") as f:
            json.dump(new_dict,f)
            print("加载入文件完成...")
        time.sleep(1)
    except:
        print("error")    

print('下载完成！') 
