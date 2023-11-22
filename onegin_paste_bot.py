import datetime as dt
import os
from time import sleep

import tweepy

# authorization:
# https://developer.twitter.com/en/portal/dashboard
consumer_key = os.environ.get('CONSUMER_KEY') or 'your-consumer-key'
consumer_secret = os.environ.get('CONSUMER_SECRET') or 'your-consumer-very-strong-secret'
access_token = os.environ.get('ACCESS_TOKEN') or 'your-access-token-which-is-also-long'
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET') or 'finally-your-access-token-here'

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


def update_pos(_pos):
    with open('current_pos', 'w') as p:
        p.write(str(_pos + 1))


months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
offset = 21     # number of days till the next iteration

os.chdir('./tweets/')
tweets = sorted(os.listdir('.'))
tweets = [t for t in tweets if '.txt' in t]
with open('current_pos') as p:
    pos = int(p.read())

if pos < len(tweets):
    stanza = tweets[pos]
    with open(stanza) as t:
        tweet = t.read().split('\\\\')

    for t in tweet:
        text = t.strip()
        # From API v1, no longer accessible: api.update_status(text, lat=57.060833, long=28.919444)
        response = client.create_tweet(text=text)
        sleep(2)  # Time in seconds.

    update_pos(pos)

elif pos == len(tweets):
    next_start = dt.date.today() + dt.timedelta(days=offset)
    day, month = str(next_start.day), months[next_start.month - 1]
    response = client.create_tweet(text=f"Следующее чтение романа начнётся {day} {month}.")
    update_pos(pos)
    with open('../iteration', 'r+') as fd_i:
        i = int(fd_i.read())
        fd_i.seek(0)
        fd_i.write(str(i + 1))
        fd_i.truncate()

elif len(tweets) < pos < len(tweets) + offset - 1:
    update_pos(pos)

else:
    with open('current_pos', 'w') as p:
        p.write('0')
