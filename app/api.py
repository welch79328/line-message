import json
import pycurl

from models.events import (
    MessageEvent,
    FollowEvent,
    UnfollowEvent,
    JoinEvent,
    LeaveEvent,
    PostbackEvent,
    BeaconEvent,
    AccountLinkEvent,
    MemberJoinedEvent,
    MemberLeftEvent,
    ThingsEvent,
)

class LineApi(object):
	
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


class LineParser(object):
	"""docstring for Parser"""
	def __init__(self):
		super().__init__()

	def parser(self, body):

		body_json = json.loads(body)
		events = []
		for event in body_json['events']:
			event_type = event['type']
			if event_type == 'message':
				events.append(MessageEvent.new_from_json_dict(event))
			elif event_type == 'follow':
				events.append(FollowEvent.new_from_json_dict(event))
			elif event_type == 'unfollow':
				events.append(UnfollowEvent.new_from_json_dict(event))
			elif event_type == 'join':
				events.append(JoinEvent.new_from_json_dict(event))
			elif event_type == 'leave':
				events.append(LeaveEvent.new_from_json_dict(event))
			elif event_type == 'postback':
				events.append(PostbackEvent.new_from_json_dict(event))
			elif event_type == 'beacon':
				events.append(BeaconEvent.new_from_json_dict(event))
			elif event_type == 'accountLink':
				events.append(AccountLinkEvent.new_from_json_dict(event))
			elif event_type == 'memberJoined':
				events.append(MemberJoinedEvent.new_from_json_dict(event))
			elif event_type == 'memberLeft':
				events.append(MemberLeftEvent.new_from_json_dict(event))
			elif event_type == 'things':
				events.append(ThingsEvent.new_from_json_dict(event))
			else:
				LOGGER.warn('Unknown event type. type=' + event_type)

		return events
		
		