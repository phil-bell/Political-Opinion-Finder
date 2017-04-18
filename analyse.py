import pymongo
import codecs
import json
import nltk
import threading
import random
from time import sleep
from pprint import pprint
from collections import Counter
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier

from display import display
from mongodb import mongo

#The analyse class contain  methods that analyse the data in the database
class analyse:
    def __init__(self,db):
        self.db = db
        self.dis = display()

    def nlktDownload(self):
        try:
            nltk.data.find("tokenizers")
        except LookupError:
            #self.dis.spinner("Downloading NLTK Data")
            print("No NLTK data found, downloading now...")
            nltk.download("all")
            #self.dis.stop()

    def featureFind(self,doc,wf):
        self.words = set(doc)
        self.feat = {}
        for self.i in wf:
            self.feat[self.i] = (self.i in self.words)
        return self.feat

    def dataSetOpinions(self):
        self.document = [(list(movie_reviews.words(fileid)),self.category)
                            for self.category in movie_reviews.categories()
                            for fileid in movie_reviews.fileids(self.category)]
        random.shuffle(self.document)

        self.all = nltk.FreqDist(self.i.lower() for self.i in movie_reviews.words())
        self.wordFeatures = [self.i for (self.i,self.c)in self.all.most_common(3000)]

        # wordFeatures = [w[0] for w in sorted(all_words.items(), key=lambda (k, v):v, reverse=True)[:3000]]

        self.featset = [(go.featureFind(self.r,self.wordFeatures),self.category) for (self.r,self.category) in self.document]

        self.trainSet = self.featset[:1000]
        self.testSet = self.featset[1000:]

        self.classifier = nltk.NaiveBayesClassifier.train(self.trainSet)
        print("Accuracy:",nltk.classify.accuracy(self.classifier,self.testSet)*100,"%")
        # self.classifier.show_most_informative_features(10)
        

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

        threading.Thread(target=self.dis.spinner, args=("Analysing Tweets ",)).start()

        self.search1 = analyse(self.db).counter(term1)
        self.search2 = analyse(self.db).counter(term2)
        
        self.dis.stop()

        print(term1,":",self.dis.joiner(self.search1["counter"]))
        print(term2, ":", self.dis.joiner(self.search2["counter"]))

        if(list(self.search2["counter"])[0] > list(self.search1["counter"])[0]):
            return term2
        return term1

    
    def searcher(self,term):
        
        threading.Thread(target=self.dis.spinner, args=("Searching Database ",)).start()
        self.tweetList = []
        self.dbout = self.db.tweets.find({})
        for self.i in self.dbout:
            if term in self.i["tweet"].lower():
                self.tweetList.append(self.i)
            if "#"+term in self.i["tweet"]:
                self.tweetList.append(self.i)
        self.dis.stop()
        return self.tweetList


    #
    def tweetMeaning(self,term):
        self.dbout = self.searcher(term)

        with open("data/words.json") as filedata:
            self.wordList = json.load(filedata)

        threading.Thread(target=self.dis.spinner, args=("Analysing Tweets ",)).start()
        self.tweetList = []
        for self.i in self.dbout:
            self.procounter = 0
            self.negcounter = 0
            for self.word in nltk.word_tokenize(self.i["tweet"]):
                #print("Analysing word: "+self.word)
                try:
                    if nltk.PorterStemmer().stem(self.word) in self.wordList["good"]:
                        #print("Found good world")
                        self.procounter = + 1
                    if nltk.PorterStemmer().stem(self.word) in self.wordList["bad"]:
                        #print("Found bad world")
                        self.negcounter = + 1
                    # if nltk.PorterStemmer().stem(self.word) in self.wordList["swear"]:
                    #     print("Found bad world")
                    #     self.negcounter = + 1
                    else:
                        self.neucounter = + 1
                except IndexError:
                    print("Ignoring tweet:",self.i["tweet"])

            self.view = "unknown"
            if self.procounter > self.negcounter:
                self.view = "pro"
            if self.negcounter > self.procounter:
                self.view = "neg"
            self.tweetDict = {
                "id": self.i["_id"],
                "tweet": self.i["tweet"],
                "procount": self.procounter,
                "negcount": self.negcounter,
                # "view":"pro" if self.procounter > self.negcounter else "neg"
                "view": self.view
            }
            self.tweetList.append(self.tweetDict)
        self.dis.stop()
        return self.tweetList
        

    def getPollData(self):
        with open("data/polls.json") as filedata:
            self.data = json.load(filedata)

        self.remainTot = 0
        self.leaveTot = 0
        self.unsureTot = 0

        for self.i in self.data["polls"]:
            self.remainTot = self.remainTot + self.i["remain"]
            self.leaveTot = self.leaveTot + self.i["leave"]
            self.unsureTot = self.unsureTot + self.i["unsure"]

        self.pollDict = {
            "remain":self.remainTot,
            "leave":self.leaveTot,
            "unsure":self.unsureTot,
            "remainPer": (self.remainTot / (self.remainTot + self.leaveTot + self.unsureTot)) * 100,
            "leavePer": (self.leaveTot / (self.remainTot + self.leaveTot + self.unsureTot)) * 100
        }
        return self.pollDict


    #This finds the most common hashtags used in the database
    def getHashtags(self):
        self.twitRes = analyse(self.db).tweetMeaning("brexit")

        threading.Thread(target=self.dis.spinner, args=("Counting Hashtags ",)).start()
        self.f = open("tweets.txt", "w")

        self.hashList = []

        for self. i in self.twitRes:
            for self.j in self.i["tweet"].split():
                if self.j[0] == "#":
                    self.hashList.append(self.j.lower())

        for self.i in Counter(self.hashList).most_common(100):
            try:
                self.f.write(self.i[0]+"\n")
            except UnicodeEncodeError:
                print("UnicodeEncodeError")

        self.dis.stop()

    def twitPollCompare(self):
        self.pollRes = analyse(self.db).getPollData()
        self.twitRes = analyse(self.db).tweetMeaning("brexit")

        threading.Thread(target=self.dis.spinner, args=("Analysing Tweets ",)).start()

        self.remainList = []
        self.leaveList = []
        self.nullList = []

        self.remainHash = ["remain", "strongerin", "voteremain", "bremain","brexitthemovie","remainineu","scotland","votein","in","labourinforbritain","eureflondon","indyref"]
        self.leaveHash = ["voteleave", "leaveeu", "takecontrol", "leave", "voteout", "betteroffout","out","takebackcontrol"]

        for self.i in self.twitRes:
            if any(self.term in self.i["tweet"].lower() for self.term in self.remainHash):
                self.remainList.append(self.i)
            elif any(self.term in self.i["tweet"].lower() for self.term in self.leaveHash):
                self.leaveList.append(self.i)
            else:
                self.nullList.append(self.i)

        self.procount = len(self.remainList)
        self.negcount = len(self.leaveList)
        self.nullcount = len(self.nullList)
        
        self.twitRemainPer = (self.procount / (self.procount + self.negcount)) * 100
        self.twitLeavePer = 100 - self.twitRemainPer
        
        self.dis.stop()

        print ("Poll Results:",
        "\n    Remain:", round(self.pollRes["remainPer"],1), "% ({})".format(self.pollRes["remain"]),
        "\n    Leave:",round(self.pollRes["leavePer"],1),"% ({})".format(self.pollRes["leave"]),
        "\nTwitter Results:",
        "\n    Remain:",round(self.twitRemainPer,1),"% ({})".format(self.procount),
        "\n    Leave:",round(self.twitLeavePer,1),"% ({})".format(self.negcount),
        "\n    Null:",self.nullcount,
        )


    # def test(self):
    #     # self.out = analyse(self.db).searcher("")
    #     # print (len(self.out))
    #     self.tweetList = []
    #     self.dbout = self.db.tweets.find({})
    #     for self.i in self.dbout:
    #         self.tweetList.append(self.i)
        
        
    #     self.counter = 0
    #     for self.i in self.tweetList:
    #         if "brexit" not in self.i["tweet"].lower():
    #             print(self.i["tweet"],"\n\n")
    #             self.counter = self.counter + 1
    #     print(len(self.tweetList))
    #     print(self.counter)

# go = analyse(mongo().conn())
# output = display()
# print(go.compare("#remain","#leave"))
# go = analyse(mongo().conn())
# go.nlktDownload()
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


go = analyse(mongo().conn())
go.dataSetOpinions()

# The top 3000 most frequent words should be obtained by:

# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = [w for (w, c) in all_words.most_common(3000)]

# If you use this as the feature, the accuracy will almost always be above 80 % and can occasionally hit 90 % .

# And thanks for the video. I have really found some cool stuff in them.﻿
