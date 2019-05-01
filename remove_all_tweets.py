#!/usr/bin/python2.6
#! encoding:utf8

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


def batch_delete(api):
    print "You are about to Delete all tweets from the account @%s." % api.verify_credentials().screen_name
    print "Does this sound ok? There is no undo! Type yes to carry out this action."
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            api.destroy_status(status.id)
            print "Deleted:", status.id

batch_delete(api)
