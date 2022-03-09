import requests
import os
ENDPOINT_TELEGRAM = "https://api.telegram.org/bot"
BOT_TOKEN = os.environ["BOT_TOKEN"]
BOT_CHAT_ID = os.environ["BOT_CHAT_ID"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message):
        self.message = message

    def send(self):
        response_telegram = requests.get(url=f"{ENDPOINT_TELEGRAM}{BOT_TOKEN}/sendMessage?chat_id={BOT_CHAT_ID}"
                                             f"&parse_mode=Markdown&text={self.message}")
        response_telegram.raise_for_status()
        return response_telegram.json()
