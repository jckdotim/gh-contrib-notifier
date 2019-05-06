import os

from notifier import check_contributions_and_notify


if __name__ == '__main__':
    check_contributions_and_notify(
        github_id=os.environ['GITHUB_ID'],
        channel_access_token=os.environ['CHANNEL_ACCESS_TOKEN'],
        to=os.environ['TO']
    )
