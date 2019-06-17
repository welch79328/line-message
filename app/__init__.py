from flask import Flask, request
import repy as Repy
import config

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/test")
def test():
	return config.CHANNEL_ACCESS_TOKEN

@app.route("/testGet", methods=['GET'])
def testGet():
	aa = request.args.get('username')
	return 'aaa'+aa

@app.route("/testPost", methods=['POST'])
def testPost():
	if request.method == 'POST':
		return 'Hello ' + request.form['username']

@app.route("/repy", methods=['POST'])
def repy():
	message = Repy.message()
	return message.run()

if __name__ == "__main__":
    app.run()