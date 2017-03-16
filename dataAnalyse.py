import pymongo
import codecs

from display import display
from mongodb import mongo

class analyse:
    def __init__(self,db):
        self.db = db

    def searcher(self, term, incremetor):
        self.tweetList = self.db.tweets.find({})
        for self.i in self.tweetList:
            if (term in self.i["tweet"]):
                print(self.i["tweet"].encode("utf-8"))
                incremetor = incremetor + 1

        self.out = {
            "list":{self.tweetList},
            "term":{term},
            "counter": {incremetor}
        }

        return self.out

    def rvl(self):
        self.remain = go.searcher("remain",0)
        output.divider(100,"=")
        self.leave = go.searcher("leave",0) 
        
        output.joiner(self.remain["counter"])
        print(self.remain["counter"])
        if(self.leave["counter"] > self.remain["counter"]):
            return "leave"
        return "remain"

go = analyse(mongo().conn())
output = display()
print(go.rvl())
