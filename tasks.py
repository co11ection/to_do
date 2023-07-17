from .celery import app
from decouple import config
import requests


@app.task
def send_email_task(text, chat_id):
    token = config
    url_request = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    result = requests.get(url_request)