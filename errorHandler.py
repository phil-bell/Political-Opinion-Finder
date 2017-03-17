import sys
import time

class errorsHandler:

    #method that makes a loading bar, is passed an lenght of time in minutes
    def loadingBar(self,time):
        for i in range(101):
            print("\rProgress: [{0:100s}] {1:.1f}%".format('#' * int(i * 1), i*1), end="", flush=True)
            time.sleep((60*time)/100)
    
    #method that makes the program wait for 15 min when the API rate limit is reached
    def limitHandler(self,cursor):
        while True:
            try:
                yield cursor.next()
            except tweepy.RateLimitError:
                loadingBar(15)



