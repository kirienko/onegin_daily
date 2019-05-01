#!/usr/bin/python2.6
#! encoding: utf8

import tweepy

# authorization:
# https://dev.twitter.com/apps
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-very-strong-secret'
access_token = 'your-access-token-which-is-also-long'
access_token_secret = 'finally-your-access-token-here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status('Привет из Михайловского', 0, 57.060833, 28.919444)
