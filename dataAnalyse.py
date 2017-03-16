import pymongo
import codecs

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
    def compare(self,item1,item2):
        self.search1 = go.searcher(item1)
        output.divider(100,"=")
        self.search2 = go.searcher(item2) 
        
        print(output.joiner(self.search1["counter"]))
        print(output.joiner(self.search2["counter"]))

        if(list(self.search2["counter"])[0] > list(self.search1["counter"])[0]):
            return item2
        return item1

go = analyse(mongo().conn())
output = display()
print(go.compare("#remain","#leave"))
