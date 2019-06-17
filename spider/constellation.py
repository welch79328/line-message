from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import sys
import os
import json
import datetime


new_dict = {"constellation": {}}

constellation_name = ['牡羊座','金牛座','雙子座','巨蟹座','獅子座','處女座','天秤座','天蠍座','射手座','摩羯座','水瓶座','雙魚座']

for number in range(12):
        value = {}
        today=datetime.date.today()
        html = urlopen('http://astro.click108.com.tw/daily_'+str(number)+'.php?iAcDay='+str(today)+'&iAstro='+str(number))
        bsObj = BeautifulSoup(html, "lxml")
        nameTitle = bsObj.find("div", {"class":"TODAY_CONTENT"}).find('h3')
        nameList = bsObj.find("div", {"class":"FORTUNE_BG"}).findAll('p')
        key = constellation_name[number]
        value.setdefault('title',nameTitle.get_text())
        aa = 0
        for  name  in  nameList:
    
                value.setdefault('content'+str(aa),name.get_text())
                aa = aa+1

        try:
                jsonFile = open(os.path.dirname(os.path.abspath(__file__))+"/json/constellation.json","r")
                fileContent = jsonFile.read()
                new_dict['constellation'].setdefault(key,value)

        except:
                print ('error')

        with open(os.path.dirname(os.path.abspath(__file__))+"/json/constellation.json","w") as f:
                json.dump(new_dict,f)
                print("加载入文件完成...")
