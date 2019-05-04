from datetime import date
import os

from flask import Flask
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import requests


app = Flask(__name__)


def check_contributions_and_notify(github_id, channel_access_token, to):
    today = date.today().strftime('%Y-%m-%d')
    contributions = requests.get(f'https://github-contributions-api.now.sh/v1/{github_id}').json()
    cont_count = [cont['count']
                  for cont
                  in contributions['contributions']
                  if cont['date'] == today][0]
    if cont_count == 0:
        line_bot_api = LineBotApi(channel_access_token)
        try:
            line_bot_api.push_message(to, TextSendMessage(text='👀'))
        except LineBotApiError as e:
            pass


@app.route('/')
def index():
    check_contributions_and_notify(
        github_id=os.environ['GITHUB_ID'],
        channel_access_token=os.environ['CHANNEL_ACCESS_TOKEN'],
        to=os.environ['TO']
    )
    return '{}'
