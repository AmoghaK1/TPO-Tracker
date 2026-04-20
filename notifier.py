import requests
import config

def send_telegram(message):
    url = f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": config.CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)