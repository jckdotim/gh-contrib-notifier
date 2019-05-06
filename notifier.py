from datetime import date

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import requests


def check_contributions_and_notify(github_id, channel_access_token, to):
    if today_contributions(github_id) == 0:
        notify(channel_access_token, to, '👀')


def today_contributions(github_id):
    today = date.today().strftime('%Y-%m-%d')
    api_url = f'https://github-contributions-api.now.sh/v1/{github_id}'
    contributions = requests.get(api_url).json()
    return [cont['count']
            for cont
            in contributions['contributions']
            if cont['date'] == today][0]


def notify(channel_access_token, to, message):
    line_bot_api = LineBotApi(channel_access_token)
    try:
        line_bot_api.push_message(to, TextSendMessage(text=message))
    except LineBotApiError:
        pass
