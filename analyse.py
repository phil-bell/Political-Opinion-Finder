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

    #The searcher find tweets in the database with with the search term handed
    #to it with. It will return the tweets the term and number of times it 
    #apeares in the database in a dictionary.
    #It must be handed:
    #   *a search term as a string
    def counter(self,term):
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

        dis = display()

        threading.Thread(target=dis.spinner, args=("Analysing Tweets ",)).start()

        self.search1 = analyse(self.db).counter(term1)
        self.search2 = analyse(self.db).counter(term2)
        
        dis.stop()

        print(term1,":",dis.joiner(self.search1["counter"]))
        print(term2, ":", dis.joiner(self.search2["counter"]))

        if(list(self.search2["counter"])[0] > list(self.search1["counter"])[0]):
            return term2
        return term1

    
    def searcher(self,term):
        dis = display()
        threading.Thread(target=dis.spinner, args=("Searching Database ",)).start()
        self.tweetList = []
        self.dbout = self.db.tweets.find({})
        for self.i in self.dbout:
            if term in self.i["tweet"]:
                self.tweetList.append(self.i)
        dis.stop()
        return self.tweetList


    #
    def tweetMeaning(self,term):
        self.dbout = self.searcher(term)

        with open("data/words.json") as filedata:
            self.wordList = json.load(filedata)

        dis = display()
        threading.Thread(target=dis.spinner, args=("Analysing Tweets ",)).start()
        self.tweetList = []
        for self.i in self.dbout:
            self.procounter = 0
            self.negcounter = 0
            for self.word in nltk.word_tokenize(self.i["tweet"]):
                #print("Analysing word: "+self.word)
                if nltk.PorterStemmer().stem(self.word) in self.wordList["good"]:
                    #print("Found good world")
                    self.procounter = + 1
                if nltk.PorterStemmer().stem(self.word) in self.wordList["bad"]:
                    #print("Found bad world")
                    self.negcounter = + 1
                if nltk.PorterStemmer().stem(self.word) in self.wordList["swear"]:
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
        dis.stop()
        return self.tweetList
        

    


# go = analyse(mongo().conn())
# output = display()
# print(go.compare("#remain","#leave"))
#go = analyse(mongo().conn())

#go.tweetMeaning("#remain")
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
