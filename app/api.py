import json
import pycurl

from models.events import (
    MessageEvent
)

class LineApi():
	
	def __init__(self, channel_access_token):
 
		self.headers = [
			'Content-Type: application/json',
			'Authorization: Bearer ' + channel_access_token
		]

	def reply_message(self, reply_token, messages):

		if not isinstance(messages, (list, tuple)):
			messages = [messages]

		data = {
			'replyToken': reply_token,
			'messages': [message.as_json_dict() for message in messages]
		}

		print(data)

		pycurl_connect = pycurl.Curl()
		pycurl_connect.setopt(pycurl.URL, 'https://api.line.me/v2/bot/message/reply')
		pycurl_connect.setopt(pycurl.POST, 1)
		pycurl_connect.setopt(pycurl.HTTPHEADER, self.headers)
		pycurl_connect.setopt(pycurl.POSTFIELDS, json.dumps(data))
		pycurl_connect.setopt(pycurl.SSL_VERIFYPEER, False)
		pycurl_connect.setopt(pycurl.SSL_VERIFYHOST, False)
		pycurl_connect.perform()


class LineParser():
	"""docstring for Parser"""
	def __init__(self):
		super().__init__()

	def parser(self, body={}):

		body_json = json.loads(body)
		events = []
		for event in body_json['events']:
			event_type = event['type']
			if event_type == 'message':
				events.append(MessageEvent.new_from_json_dict(event))
			else:
				LOGGER.warn('Unknown event type. type=' + event_type)

		return events
		
		