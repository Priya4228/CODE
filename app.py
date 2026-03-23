from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!If you can see this, the code has been deployed to your webapp. Test to see if all pipelines run again 2x"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook received!")
    print(data)
    return "", 200
