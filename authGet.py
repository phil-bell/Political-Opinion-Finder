# This file connects to the twitter api and returns the api to 
# where it is called. It uses my api keys to be allowed acces 
# to the twitter api.

import tweepy

# this is the function that is called to connect to the api
# and return the operator for accessing it.

class twitterAPI:

    #authentigate must be handed conCheck bool value, if true it will show connection status message will be output.
    def authentigate(self,conCheck):

        #sets my consumer keys to auth.
        self.auth = tweepy.OAuthHandler("esOD1d4qKPys3fjwFrrMxevGv", "ClhLgKumBTKUYosji5tUreMwTZGN84hBb0XDhB9ouKXRsqkXHq")
                                        #^^Consumer Key^^           #^^Consumer Secret^^
        
        #sets the appliction access keys to my consumer key.
        self.auth.set_access_token("188453340-AsHcJSD3pCo2s4Ya6rOjJYXlW2ZiMARVa0xX8scY", "EQGTXpt507XS42sRTHs4son7bBc0UHhilaDoggfRW8KpZ")
                                    #^^Access Token^^                                     #^^Access Token Secret^^
        
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
