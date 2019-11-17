import json
from flask import Flask, request, abort

from api import (
    LineApi, LineParser
)

from models import (
    TextSendMessage, ImageSendMessage, VideoSendMessage
)

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "ZT0xaLhXoVui97bktWgEdJaGFz6G1Y+TARALFznkFQCoQuzb4zcT69ZJzqtkV5xKgTFpqbCjeXa0X47kVJoGTosT+q+nvMn3Afc3hwBG3QpuDe5LN5qhGzH56R5iMtlgBCNGqEnUV/Eew8NFv0l9AQdB04t89/1O/w1cDnyilFU="

line_api = LineApi(CHANNEL_ACCESS_TOKEN)
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
			message = TextSendMessage("文字")

		if event.message.text == "圖片":
			original_content_url="https://adot.com.tw/message/images/13.jpg"
			preview_image_url="https://adot.com.tw/message/images/13.jpg"
			message = ImageSendMessage(original_content_url, preview_image_url)

		if event.message.text == "影片":
			original_content_url="https://webrtc.github.io/samples/src/video/chrome.webm"
			preview_image_url="https://webrtc.github.io/samples/src/video/chrome.webm"
			message = VideoSendMessage(original_content_url, preview_image_url)

		line_api.reply_message(
			event.reply_token,
			message
		)

	return "OK"

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)