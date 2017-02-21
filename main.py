import tweepy
import authGet

api = authGet.authentigate()

public_tweet = api.home_timeline()
for tweet in public_tweet:
    out = tweet.text
    print (out.encode("utf-8"))

