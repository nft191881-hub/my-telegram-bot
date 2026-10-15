import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 填入你的新 Token
BOT_TOKEN = "8798836806:AAFU7B6KLk-WcFlDOee6ey9kTg4Db-FryJI"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# 对应根目录绑定，直接接收 Telegram 发来的消息
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"status": "ok"})
    
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')
    
    if text == '/start':
        payload = {
            "chat_id": chat_id,
            "text": "欢迎来到 TG 商城/钱包！请点击下方按钮打开应用：",
            "reply_markup": {
                "inline_keyboard": [
                    [
                        {
                            "text": "🚀 打开商城/钱包",
                            "web_app": {"url": "https://my-telegram-bot-beryl-three.vercel.app"}
                        }
                    ]
                ]
            }
        }
        requests.post(f"{TELEGRAM_API}/sendMessage", json=payload)
        
    return jsonify({"status": "success"})

@app.route('/', methods=['GET'])
def index():
    return "Telegram Bot is running!"

app = app
