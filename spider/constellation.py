from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import sys
import os
import json
import datetime


new_dict = {"constellation": {}}

#constellation_name = ['牡羊座','獅子座','射手座','金牛座','處女座','摩羯座','雙子座','天秤座','水瓶座','巨蟹座','天蠍座','雙魚座']

#constellation_list = ['Aries','Leo','Sagittarius','Taurus','Virgo','Capricorn','Gemini','Libra','Aquarius','Cancer','Scorpio','Pisces']

constellation_list = {'Aries':'牡羊座','Leo':'獅子座','Sagittarius':'射手座','Taurus':'金牛座','Virgo':'處女座','Capricorn':'摩羯座','Gemini':'雙子座','Libra':'天秤座','Aquarius':'水瓶座','Cancer':'巨蟹座','Scorpio':'天蠍座','Pisces':'雙魚座'}

for constellation in constellation_list:
        value = {}
        today=datetime.date.today()
        html = urlopen('https://www.daily-zodiac.com/mobile/zodiac/'+str(constellation))
        bsObj = BeautifulSoup(html, "lxml")
        content = bsObj.find("div", {"class":"text"}).find("article")
        key = constellation_list[constellation]
        value.setdefault('content',content.get_text())
 
        try:
                jsonFile = open(os.path.dirname(os.path.abspath(__file__))+"constellation.json","r")
                fileContent = jsonFile.read()
                new_dict['constellation'].setdefault(key,value)

        except:
                print ('error')

        with open(os.path.dirname(os.path.abspath(__file__))+"constellation.json","w") as f:
                json.dump(new_dict,f)
                print("加载入文件完成...")
