import pymongo
import codecs
import json
import nltk
import threading
from time import sleep
from pprint import pprint

from display import display
from mongodb import mongo

#The analyse class contain  methods that analyse the data in the database
class analyse:
    def __init__(self,db):
        self.db = db

    def spinner(self):
        global stopper
        while stopper == True:
            print("Analysing Tweets [\]", end="\r")
            sleep(.1)
            print("Analysing Tweets [|]", end="\r")
            sleep(.1)
            print("Analysing Tweets [/]", end="\r")
            sleep(.1)
            print("Analysing Tweets [—]", end="\r")
            sleep(.1)
        print("Complete...              ")
        

    #The searcher find tweets in the database with with the search term handed
    #to it with. It will return the tweets the term and number of times it 
    #apeares in the database in a dictionary.
    #It must be handed:
    #   *a search term as a string
    def searcher(self,term):
        self.incremetor = 0
        self.tweetList = self.db.tweets.find({})
        for self.i in self.tweetList:
            if (term in self.i["tweet"]):
                #print(self.i["tweet"].encode("utf-8"))
                self.incremetor = self.incremetor + 1

        self.out = {
            "list":{self.tweetList},
            "term":{term},
            "counter": {self.incremetor}
        }

        return self.out

    #compare() compairs if people tweet about one thing or another more
    #it returns the winner.
    #It must be handed:
    #   *First term to compare as a string
    #   *Second term to compare as a string
    def compare(self,term1,term2):
        global stopper

        stopper = True
        threading.Thread(target=go.spinner, args=()).start()

        self.search1 = go.searcher(term1)
        self.search2 = go.searcher(term2) 

        stopper = False
        sleep(.5)

        print(term1,":",display().joiner(self.search1["counter"]))
        print(term2, ":", display().joiner(self.search2["counter"]))

        if(list(self.search2["counter"])[0] > list(self.search1["counter"])[0]):
            return term2
        return term1

    #
    def tweetMeaning(self,term):
        global stopper
        self.dbout = self.db.tweets.find({})

        with open("data/words.json") as filedata:
            self.wordList = json.load(filedata)

        stopper = True
        threading.Thread(target=go.spinner, args=()).start()
        self.tweetList = []
        for self.i in self.dbout:
            self.procounter = 0
            self.negcounter = 0
            #print("Analysing tweet: "+self.i["tweet"])
            for self.word in self.i["tweet"].split():
                #print("Analysing word: "+self.word)
                if self.word in self.wordList["good"]:
                    #print("Found good world")
                    self.procounter = + 1
                if self.word in self.wordList["bad"]:
                    #print("Found bad world")
                    self.negcounter = + 1
                if self.word in self.wordList["swear"]:
                    #print("Found bad world")
                    self.negcounter = + 1
            self.tweetDict = {
                "id": self.i["_id"],
                "tweet": self.i["tweet"],
                "procount": self.procounter,
                "negcount": self.negcounter,
                "view":"pro" if self.procounter >= self.negcounter else "neg"
            }
            self.tweetList.append(self.tweetDict)
        stopper = False
        return self.tweetList


# go = analyse(mongo().conn())
# output = display()
# print(go.compare("#remain","#leave"))

stopper = True
go = analyse(mongo().conn())

# out = go.tweetMeaning("#remain")

# print(out["view"])
# print(out["badcount"])
# print(out["goodcount"])
# print(out["tweet"])

# self.tweetDict = {
#     "tweet":[],
#     "procount":[],
#     "negcount":[],
#     "view":[]
# }
# for self.i in self.dbout:
#     self.procounter = 0
#     self.negcounter = 0
#     for self.word in self.i["tweet"]:
#         if self.word in self.wordList["good"]:
#             self.procounter = + 1
#         if self.word in self.wordList["bad"]:
#             self.negcounter = + 1
#         if self.word in self.wordList["swear"]:
#             self.negcounter = + 1
#     self.tweetDict["tweet"].append(self.i["tweet"])
#     self.tweetDict["procounter"].append(self.procounter)
#     self.tweetDict["negcounter"].append(self.procounter)
#     if self.procounter > self.negcounter:
#         self.tweetDict.append("pro")
#     else:
#         self.tweetDict.append("neg")
