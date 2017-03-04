# This is the main file, it gets tweets with the #brexit hashtag 
# and puts them in a mongoDB with the tweet, username, who they
# follows and who follows them.  

import tweepy #Twitter API library
import codecs #encoding library for encodeding tweets in utf-8
import pymongo #mongo library
import time
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

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print ("Waiting...")
            time.sleep(15)

#gets tweets from hashtag "#brexit" and puts them in the mongo database
def getTweets(api,db):
    brexitTweets = tweepy.Cursor(api.search,q="#brexit",show_user=True,locale=True,wait_on_rate_limit=True).items()

    #loops through the list of tweetsco
    for tweets in brexitTweets:

        out = tweets.text
        name = tweets.author.screen_name
        followers = []
        friends = []
        tmp = 0

        #gets the users followers and puts them in a list
        #for users in tweepy.Cursor(api.followers, screen_name=name,wait_on_rate_limit=True,wait_on_rate_limit_notify=True).items():
            #print ("Adding to followers list: ",users.screen_name)
            #followers.append(users.screen_name)
        
        #gets the users following and puts them in the list
        #for users in tweepy.Cursor(api.friends, screen_name=name,wait_on_rate_limit=True,wait_on_rate_limit_notify=True).items():
            #print ("Adding to friends list: ",users.screen_name)
            #friends.append(users.screen_name)

        print ("\n\nAdded: ","\n    Username: ",name,"\n    Followers: ",followers,"\n    Following",friends,"\n    Tweets:",out.encode("utf-8")) #shows tweets being added to the DB
        
        #adds the data to the database
        results = db.tweets.insert_one(
            {
                "username":name,
                #"followers":followers,
                #"friends":friends,
                "tweet":out
                
            }
        )

        
getTweets(api,db) #calls the function that gets tweets and puts them in the DB