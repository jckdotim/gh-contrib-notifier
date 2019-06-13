import os

from notifier import check_contributions_and_notify


if __name__ == '__main__':
    required_keys = ('GITHUB_ID', 'CHANNEL_ACCESS_TOKEN', 'TO')
    if not all(k in os.environ for k in required_keys):
        print(f'''
            You need to specify following environment variables:
            {",".join(required_keys)}
        ''')
        exit(1)
    check_contributions_and_notify(
        github_id=os.environ['GITHUB_ID'],
        channel_access_token=os.environ['CHANNEL_ACCESS_TOKEN'],
        to=os.environ['TO']
    )
