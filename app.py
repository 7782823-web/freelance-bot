from flask import Flask, request, jsonify
import requests
import os
app = Flask(__name__)
WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/oc_d6320885048ca26f33d2c51933257707"
@app.route("/")
def index(): return "AI Bot Running!"
@app.route("/feishu/webhook", methods=["POST"])
def webhook(): return jsonify({"status":"ok"}),200
if __name__ == "__main__": app.run(host="0.0.0.0",port=int(os.getenv("PORT",5000)))
