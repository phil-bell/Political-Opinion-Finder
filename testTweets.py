#This file is for testing methods
import codecs
from authGet import twitterAPI
from display import display

class testing:
    def __init__():
        self.api = twitterAPI().authentigate(False)

    #gets random tweets as a test
    def pubTweets(api):
        self.publicTweet = self.api.home_timeline()
        for self.tweets in self.publicTweet:
            self.out = self.tweets.text
            print (self.out.decode("utf-8").encode('cp850','replace').decode('cp850'))
        display().divider(50,"=")