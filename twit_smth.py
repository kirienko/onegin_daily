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

api.update_status('Привет из Михайловского', lat=57.060833, long=28.919444)
