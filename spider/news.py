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

html = urlopen('https://www.nownews.com/')
bsObj = BeautifulSoup(html, "lxml")
filepath = os.path.dirname(os.path.abspath(__file__))

news_list = bsObj.findAll("div", {"class":"td-block-span6"})
key = 0
for news in news_list:
	value = {}
	href = news.find('a')['href']
	img = news.find('img')
	title = news.find('a')['title']
	img_url1 = img['src'].split("w=100&q=70&", 1)
	img_url2 = img_url1[1].split("-100x70", 1)
	img_url = img_url1[0] + img_url2[0] + img_url2[1]

	value['href'] = href
	value['title'] = title

	try:
		# 記得更改想要下載到的位
		file_name = int(time.time())+random.randint(0,1000)
		value['img_url'] = str(file_name)+'.jpg'
		if not os.path.exists(filepath+"/file/news/"):
			os.makedirs(filepath+"/file/news/")
			os.chmod(filepath+"/file/news/", 0o777)

		if not os.path.exists(filepath+"/json/news.json"): 
			open(filepath+"/json/news.json","w")

		urlretrieve(img_url, filepath+'/file/news/'+str(file_name)+'.jpg')
		try:
			jsonFile = open(filepath+"/json/news.json","r")
			if jsonFile == False:
				fileContent = jsonFile.read()
				new_dict = json.loads(fileContent)
			new_dict['news'].setdefault(key,value)
			key = key + 1
		except:
			print ('error')

		with open(filepath+"/json/news.json","w") as f:
			json.dump(new_dict,f)
			print("加载入文件完成...")
	except:
		print('{} {}_{}.jpg 下載失敗!')