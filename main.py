# This is the main file, it gets tweets with the #brexit hashtag 
# and puts them in a mongoDB with the tweet, username, who they
# follows and who follows them.  

import tweepy #Twitter API library
import codecs #encoding library for encodeding tweets in utf-8
import pymongo #mongo library
import time
import got3 #library that allows search for legacy tweets, written by Jefferson Henrique (https://github.com/Jefferson-Henrique/GetOldTweets-python)
from pymongo import MongoClient #gets the mongo client method

#imports local files
import authGet
import mongodb
import locGet


#gets twitter api and mongo connection
api = authGet.authentigate()
db = mongodb.conn()

#gets tweets from hashtag "#brexit" and puts them in the mongo database
def getTweets(api,db,hashtag):

    #CVS for later: -8.23,49.93,1.74,60.84
    #CVS RAW for later: -8.2287597656,49.9300081246,1.7358398437,60.8449105736

    tweetCriteria = got3.manager.TweetCriteria().setQuerySearch(hashtag).setSince("2016-06-12").setUntil("2016-06-13").setMaxTweets(2)
    brexitTweets = got3.manager.TweetManager.getTweets(tweetCriteria)

    #brexitTweets = tweepy.Cursor(api.search,q="#brexit",show_user=True,locale=True,wait_on_rate_limit=True).items()

    #loops through the list of tweetsco
    for tweets in brexitTweets:

        out = tweets.text
        name = tweets.username
        uid = tweets.id
        date = tweets.date
        geo = locGet.locFind(name)
        followers = []
        friends = []
        tmp = 0
        
        #gets the users followers id and puts them in a list
        for users in tweepy.Cursor(api.followers_ids, screen_name=name,wait_on_rate_limit=True,wait_on_rate_limit_notify=True).items(1):
            #print ("Adding to followers list: ",users)
            followers.append(users)
        
        #gets the users following and puts them in the list
        #for users in tweepy.Cursor(api.friends, screen_name=name,wait_on_rate_limit=True,wait_on_rate_limit_notify=True).items():
            #print ("Adding to friends list: ",users.screen_name)
            #friends.append(users.screen_name)

        print ("\n\nAdded:","\n    Username:",name,"\n    User ID:",uid,"\n    Date:",date,"\n    Location:",geo,"\n    Followers:",followers,"\n    Tweets:",out.encode("utf-8")) #shows tweets being added to the DB
        
        #adds the data to the database

        results = db.tweets.insert_one(
            {
                "username":name,
                "userID":uid,
                "date":date,
                "location:":geo,
                "followers":followers,
                #"friends":friends,
                "tweet":out
                
            }
        )

getTweets(api,db,"#brexit") #calls the function that gets tweets and puts them in the DB