"""
Nowadays twitter provides much better statistics.
Therefore you don't need to use this anymore.
"""

from datetime import date

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
user = api.get_user(screen_name='onegin_daily')
date = date.today().isoformat()
flwrs = user.followers_count
with open('/home/my_user/onegin/stat/followers.log', 'a') as fd:
    fd.write("%s %d\n" % (date, flwrs))
