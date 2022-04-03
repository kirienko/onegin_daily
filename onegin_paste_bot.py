import datetime as dt
import os
from time import sleep

import tweepy

# authorization:
# https://dev.twitter.com/apps
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-very-strong-secret'
access_token = 'your-access-token-which-is-also-long'
access_token_secret = 'finally-your-access-token-here'

auth = tweepy.OAuth1UserHandler(consumer_key=consumer_key,
                                consumer_secret=consumer_secret,
                                access_token=access_token,
                                access_token_secret=access_token_secret)
api = tweepy.API(auth)


def update_pos(_pos):
    with open('current_pos', 'w') as p:
        p.write(str(_pos + 1))


months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
offset = 21     # число дней до следующей итерации

os.chdir('/home/my_user/onegin/tweets/')
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
        api.update_status(text, lat=57.060833, long=28.919444)
        sleep(2)  # Time in seconds.

    update_pos(pos)

elif pos == len(tweets):
    next_start = dt.date.today() + dt.timedelta(days=offset)
    day, month = str(next_start.day), months[next_start.month - 1]
    api.update_status(f"Следующее чтение романа начнётся {day} {month}.", lat=59.9395, long=30.3284)
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
