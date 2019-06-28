import json
from flask import Flask, request

from api import (
    LineApi, LineParser
)

from models import (
    TextSendMessage
)

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "ANWmBORlSQhnmfriPxH+Y7bwBxD+p2qnCJgrMC4Ipwe4z33cWCP68HE1Y2SFdw7WgTFpqbCjeXa0X47kVJoGTosT+q+nvMn3Afc3hwBG3QobxmaFHEN9np2HcboImqjUWLipDBZTK7EEtfwU1YLJiwdB04t89/1O/w1cDnyilFU="

line_api = LineApi(CHANNEL_ACCESS_TOKEN)
parser = LineParser()

@app.route("/")
def hello():
	body = "Hello, I love Digital Ocean!"
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	return body

@app.route("/repy", methods=['GET','POST'])
def repy():
	body = request.get_data(as_text=True)
	events = parser.parser(body)

	for event in events:
		line_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

	return "OK"