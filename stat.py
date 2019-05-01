#!/usr/bin/python2.6
#! encoding: utf8

import tweepy
from datetime import date

# authorization:
# https://dev.twitter.com/apps
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-very-strong-secret'
access_token = 'your-access-token-which-is-also-long'
access_token_secret = 'finally-your-access-token-here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
date = date.today().isoformat()
flwrs = user.followers_count
with open('/home/my_user/onegin/stat/followers.log', 'a') as fd:
    fd.write("%s %d\n" % (date, flwrs))
