from flask import request
import json
import os
import pycurl
import config

class message():
	def __init__(self):
		self.CHANNEL_ACCESS_TOKEN = config.CHANNEL_ACCESS_TOKEN
		self.text = ''
		self.payload = {}
		self.sendMessageStatus = False
		
	def getMessage(self):
		body = json.loads(request.get_data(as_text=True))
		return body

	def messageProcess(self, body):
		for event in body['events']:
			replyToken = event['replyToken']

			if 'userId' in event['source']:
				userId = event['source']['userId']

			if 'text' in event['message']:
				text = event['message']['text']

			payload = self.messageLogic(text, replyToken)

			if self.sendMessageStatus:
				self.sendMessage(payload)

	def sendMessage(self, payload):

		pycurl_connect = pycurl.Curl()
		pycurl_connect.setopt(pycurl.URL, 'https://api.line.me/v2/bot/message/reply')
		pycurl_connect.setopt(pycurl.POST, 1)
		pycurl_connect.setopt(pycurl.HTTPHEADER, [
			'Content-Type: application/json',
			'Authorization: Bearer ' + self.CHANNEL_ACCESS_TOKEN
			])
		pycurl_connect.setopt(pycurl.POSTFIELDS, json.dumps(payload))
		pycurl_connect.setopt(pycurl.SSL_VERIFYPEER, False)
		pycurl_connect.setopt(pycurl.SSL_VERIFYHOST, False)
		pycurl_connect.perform()

	def run(self):
		self.messageProcess(self.getMessage())

		return 'OK'

	def messageLogic(self, text, replyToken):
		payload = {}
		if text == '222':
			payload = {
				"replyToken":replyToken,
				"messages":[
					{
						"type":"text",
						"text":"wwww"
					}
				]
			}
			self.sendMessageStatus = True

		return payload

