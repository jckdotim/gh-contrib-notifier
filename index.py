import os

from notifier import check_contributions_and_notify
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    check_contributions_and_notify(
        github_id=os.environ['GITHUB_ID'],
        channel_access_token=os.environ['CHANNEL_ACCESS_TOKEN'],
        to=os.environ['TO']
    )
    return '{}'
