# This is the main file, it gets tweets with the #brexit hashtag 
# and puts them in a mongoDB with the tweet, username, who they
# follows and who follows them.  

import tweepy #Twitter API library
import codecs #encoding library for encodeding tweets in utf-8
import pymongo #mongo library
import time
import urllib
import json
import got3 #library that allows search for legacy tweets. Written by Jefferson Henrique (https://github.com/Jefferson-Henrique/GetOldTweets-python). Nothing in the got3 (GetOldTweets3) folder is written by me and I do not claim to have done!
from pymongo import MongoClient #gets the mongo client method

#imports local files
from authGet import twitterAPI
from mongodb import mongo
from locGet import geo
from collection import collection


#gets twitter api and mongo connection

class Main:
    def __init__(self,api,db):
        self.api = api
        self.db = db

    def menu(self):
        self.userAnswer = input("What would you like to do:\n    1)Gather tweets into the database.\n    2)Find if #brexit or #remain is used more\n    3)Estimate what people will vote from tweets.\n    4)Compare twitter opinion to poll opinions.")
        if (self.userAnswer == "1"):
            coll.getTweets("#brexit")
        elif (self.userAnswer == "2"):
            anas.compare("#remain","#leave")
        elif (self.userAnswer == "3"):
            pass
        elif (self.userAnswer == "4"):
            pass
        else:
            print("Plase enter a valid input (1,2,3,4).")
            go.menu()
        return 0

twit = twitterAPI()
mong = mongo()
anas = analyse(mong.conn())
coll = collection(twit.authentigate(True), mong.conn())
go = Main(twit.authentigate(True),mong.conn())
go.menu() #calls the function that gets tweets and puts them in the DB
