from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import sys
import os
import json


#目標頁面
#citys = {'台北市':'Taipei_City','新北市':'New_Taipei_City','桃園市':'Taoyuan_City','台中市':'Taichung_City',
#		'台南市':'Tainan_City','高雄市':'Kaohsiung_City','基隆市':'Keelung_City','新竹市':'Hsinchu_City',
#		'新竹縣':'Hsinchu_County','苗栗縣':'Miaoli_County','彰化縣':'Changhua_County','南投縣':'Nantou_County',
#		'雲林縣':'Yunlin_County','嘉義市':'Chiayi_City','嘉義縣':'Chiayi_County','屏東縣':'Pingtung_County',
#		'宜蘭縣':'Pingtung_County','花蓮縣':'Hualien_County','台東縣':'Taitung_County','澎湖縣':'Penghu_County'}

citys = {'Taipei_City','New_Taipei_City','Taoyuan_City','Taichung_City',
		'Tainan_City','Kaohsiung_City','Keelung_City','Hsinchu_City',
		'Hsinchu_County','Miaoli_County','Changhua_County','Nantou_County',
		'Yunlin_County','Chiayi_City','Chiayi_County','Pingtung_County',
		'Pingtung_County','Hualien_County','Taitung_County','Penghu_County'}


new_dict = {"weather": {}}

for city in citys:
	value = {}
	html = urlopen('https://www.cwb.gov.tw/V7/forecast/taiwan/'+city+'.htm')
	bsObj = BeautifulSoup(html, "lxml")
	nameList = bsObj.find("table", {"class":"FcstBoxTable01"}).findAll('tr')
	for  name  in  nameList:
		try:
			th = name.find("th", {"scope":"row"})
			tds = name.findAll("td")
			th_name = str(th.get_text())
			#print (th.get_text())
			
			value[th_name] = {}
			
			aa = 0
		except:
			key = name.find("th").get_text()
		
		for td in tds:
			try:
				#print (td.find("img").attrs['title'])
				bb = td.find("img").attrs['title']
			except:
				#print (td.get_text())
				bb = td.get_text()
				
			if aa == 0:
				value[th_name]['temperature'] = bb
			elif aa == 1:
				value[th_name]['situation'] = bb
			elif aa == 2:
				value[th_name]['comfortable'] = bb	
			elif aa == 3:
				value[th_name]['rain'] = bb		
				
			aa = aa + 1
		
#	print (key)
#	print (value)
	try:
		print(os.path.dirname(os.path.abspath(__file__))+"/json/weather.json")
		jsonFile = open(os.path.dirname(os.path.abspath(__file__))+"/json/weather.json","r")
		fileContent = jsonFile.read()
		new_dict['weather'].setdefault(key,value)

	except:
		print ('error')

	with open(os.path.dirname(os.path.abspath(__file__))+"/json/weather.json","w") as f:
		json.dump(new_dict,f)
		print("加载入文件完成...")
