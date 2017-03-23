#This file is used for geolocation methods
#UK CVS for later: -8.23,49.93,1.74,60.84
#UK CVS RAW for later: -8.2287597656,49.9300081246,1.7358398437,60.8449105736
import tweepy
from authGet import twitterAPI

#geo class for geolocation related methods
class geo:
    def __init__(self):
        self.api = twitterAPI().authentigate(False)
    
    #gets a users location from there username(must be handed username), returns geolocation coordinates 
    def locFind(self,user):
        try:
            self.userInfo = self.api.get_user(user)
            self.userLocation = self.userInfo.location
            return self.userLocation
        except tweepy.TweepError:
            return "USER SUSPENDED"

