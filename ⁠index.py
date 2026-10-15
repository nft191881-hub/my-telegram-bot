import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 替换为你的新 Bot Token
BOT_TOKEN = "8982119906:AAG21opgx42WFhHNIjldrcbipiZx4JNXDfI"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/api/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"status": "ok"})
    
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')
    
    if text == '/start':
        # 发送带有内联网页按钮的欢迎消息
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

if __name__ == '__main__':
    app.run(debug=True)
