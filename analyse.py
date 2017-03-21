import pymongo
import codecs
import json

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
    def searcher(self,term):
        self.incremetor = 0
        self.tweetList = self.db.tweets.find({})
        for self.i in self.tweetList:
            if (term in self.i["tweet"]):
                print(self.i["tweet"].encode("utf-8"))
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
        self.search1 = go.searcher(term1)
        output.divider(100,"=")
        self.search2 = go.searcher(term2) 
        
        print(output.joiner(self.search1["counter"]))
        print(output.joiner(self.search2["counter"]))

        if(list(self.search2["counter"])[0] > list(self.search1["counter"])[0]):
            return term2
        return term1

    
    def tweetMeaning(self,term):
        self.search = go.searcher(term)
        self.tweetdict = {
            "tweet":[],
            "goodcount":[],
            "badcount":[],
            "view":[]
        }
        with open("data/words.json") as filedata:
            self.wordList = json.load(filedata)
        for self.i in self.search["list"]:
            self.procounter = 0
            self.negcounter = 0
            for self.word in self.i:
                if self.word in self.wordList["good"]:
                    self.procounter =+ 1
                if self.word in self.wordList["bad"]:
                    self.negcounter =+ 1
                if self.word in self.wordList["swear"]:
                    self.negcounter = + 1
            self.tweetdict["tweet"].append(search["list"])
            self.tweetdict["goodcount"].append(self.procounter)
            self.tweetdict["badcount"].append(self.negcounter)
            if (self.procounter > self.negcounter):
                self.tweetdict["view"].append("pro")
            else:
                self.tweetdict["view"].append("neg")
        return self.tweetdict
"""
go = analyse(mongo().conn())
output = display()
print(go.compare("#remain","#leave"))
"""