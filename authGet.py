# This file connects to the twitter api and returns the api to 
# where it is called. It uses my api keys to be allowed acces 
# to the twitter api.

import tweepy
import json

# this is the function that is called to connect to the api
# and return the operator for accessing it.

class twitterAPI:

    #authentigate must be handed conCheck bool value, if True it will show connection status message.
    def authentigate(self,conCheck):

        #gets data from json file
        with open("credentials/apiCredentials.json") as dataFile:
            cred = json.load(dataFile)

        #sets my consumer keys to auth.
        self.auth = tweepy.OAuthHandler(cred["applicationKeys"][0]["consumerKey"],cred["applicationKeys"][0]["consumerSecret"])
                                        #^^Consumer Key^^                         #^^Consumer Secret^^
        
        #sets the application access keys to my consumer key.
        self.auth.set_access_token(cred["accessTokens"][0]["accessToken"],cred["accessTokens"][0]["accessTokenSecret"])
                                    #^^Access Token^^                     #^^Access Token Secret^^
        
        #sends api keys to authenticator and returns access operator to the var api.
        self.api = tweepy.API(self.auth)
        
        if (conCheck == True):
            #tries to access the api and returns it is working if it does
            try:
                self.redirect_url = self.auth.get_authorization_url()
                if (self.redirect_url != None):
                    print("API WORKING!")
                    
            #shows no access to api if try doesnt work.
            except:
                print("Authentication Failed!")

        #returns the api operator var
        return self.api
