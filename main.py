# This is the main file, it gets tweets with the #brexit hashtag 
# and puts them in a mongoDB with the tweet, username, who they
# follows and who follows them.  

import tweepy #Twitter API library
import codecs #encoding library for encodeding tweets in utf-8
import pymongo #mongo library
from pymongo import MongoClient #gets the mongo client method

#imports local files
import authGet
import mongodb


#gets twitter api and mongo connection
api = authGet.authentigate()
db = mongodb.conn()


#gets random tweets as a test
def pubTweets(api):
    publicTweet = api.home_timeline()
    for tweets in publicTweet:
        out = tweets.text
        print (out.decode("utf-8").encode('cp850','replace').decode('cp850'))

    print ("======================================================")


#gets tweets from hashtag "#brexit" and puts them in the mongo database
def getTweets(api,db):
    brexitTweets = tweepy.Cursor(api.search,q="#brexit",show_user=True,locale=True).items(10)

    #loops through the list of tweets
    for tweets in brexitTweets:
        out = tweets.text
        name = tweets.author.screen_name
        print ("\nAdded: ",name,"-",out.encode("utf-8")) #shows tweets being added to the DB
        
        results = db.tweets.insert_one(
            {
                "username":name,
                "tweet":out
            }
        )

        
getTweets(api,db) #calls the function that gets tweets and puts them in the DB