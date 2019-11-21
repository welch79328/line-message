import json
from flask import Flask, request, abort

from __config__ import __channelAccessToken__

from api import (
    LineApi, LineParser
)

from models import (
    TextSendMessage, ImageSendMessage, VideoSendMessage
)

app = Flask(__name__)

line_api = LineApi(__channelAccessToken__)
parser = LineParser()

@app.route("/")
def hello():
	return "Hello"

@app.route("/reply", methods=['POST'])
def reply():

	body = request.get_data(as_text=True)
	try:
		events = parser.parser(body)
	except:
		abort(400)

	for event in events:
		if event.message.text == "文字":
			reply = TextSendMessage("文字")

		if event.message.text == "圖片":
			original_content_url=""
			preview_image_url=""
			reply = ImageSendMessage(original_content_url, preview_image_url)

		if event.message.text == "影片":
			original_content_url=""
			preview_image_url=""
			reply = VideoSendMessage(original_content_url, preview_image_url)

		line_api.reply_message(
			event.reply_token,
			reply
		)

	return "OK"

if __name__ == '__main__':
    app.run(debug=True)