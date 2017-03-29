# This is the main file, it gets tweets with the #brexit hashtag 
# and puts them in a mongoDB with the tweet, username, who they
# follows and who follows them.  

import tweepy #Twitter API library
import codecs #encoding library for encodeding tweets in utf-8
import pymongo #mongo library
from time import sleep
import urllib
import json
import threading
import got3 #library that allows search for legacy tweets. Written by Jefferson Henrique (https://github.com/Jefferson-Henrique/GetOldTweets-python). Nothing in the got3 (GetOldTweets3) folder is written by me and I do not claim to have done! UPDATE: GOT no longer works and I am using a version of it that I maintain my self ()
from pymongo import MongoClient #gets the mongo client method

#imports local files
from authGet import twitterAPI
from mongodb import mongo
from locGet import geo
from analyse import analyse
from collection import collection
from display import display


#gets twitter api and mongo connection

class Main:
    def __init__(self,api,db):
        self.api = api
        self.db = db

    def menu(self):
        sleep(1)
        self.userAnswer = input("What would you like to do:"+
        "\n    1)Gather tweets into the database."+
        "\n    2)Find if #X or #Y is used more."+
        "\n    3)Find Twitters opinion on a hashtag"+
        "\n    4)Estimate what people will vote from tweets."+
        "\n    5)Compare twitter opinion to poll opinions."+
        "\nEnter: ")
        if (self.userAnswer == "1"):
            coll.getTweets("#brexit")
        elif (self.userAnswer == "2"):
            self.u1 = input("First term: ")
            self.u2 = input("Second term: ")
            print(anas.compare(self.u1,self.u2),"is used more")
        elif (self.userAnswer == "3"):
            self.input = input("What term would you like to evaluate: ")
            self.out = anas.tweetMeaning(self.input)
            self.procount = 0
            self.negcount = 0
            for self.i in self.out:
                if (self.i["view"] == "pro"):
                    self.procount = self.procount + 1
                else:
                    self.negcount = self.negcount + 1
            print("Tweets for:",self.procount)
            print("Tweets against:",self.negcount)
            if self.procount > self.negcount:
                print("Twitter user are in favor of:",self.input)
            else:
                print("Twitter user are not in favor of:", self.input)
        elif (self.userAnswer == "4"):
            pass
        else:
            print("Plase enter a valid input (1,2,3,4,5).")
            go.menu()
        return 0


dis = display()
threading.Thread(target=dis.slider, args=("Connecting ",)).start()
twit = twitterAPI()
mong = mongo()
anas = analyse(mong.conn())
coll = collection(twit.authentigate(False), mong.conn())
go = Main(twit.authentigate(False),mong.conn())
dis.stop()
go.menu() #calls the function that gets tweets and puts them in the DB
