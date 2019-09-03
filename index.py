import os

from notifier import check_contributions_and_notify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:////tmp/test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    github_id = db.Column(db.String, primary_key=True)
    line_uid = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.github_id


@app.route('/')
def index():
    for user in User.query:
        check_contributions_and_notify(
            github_id=user.github_id,
            channel_access_token=os.environ['CHANNEL_ACCESS_TOKEN'],
            to=user.line_uid
        )
    return '{}'
