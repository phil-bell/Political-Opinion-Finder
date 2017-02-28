# This file connects to the twitter api and returns the api to 
# where it is called. It uses my api keys to be allowed acces 
# to the twitter api.

import tweepy

# this is the function that is called to connect to the api
# and return the operator for accessing it.
def authentigate():

    #sets my consumer keys to auth.
    auth = tweepy.OAuthHandler("esOD1d4qKPys3fjwFrrMxevGv", "ClhLgKumBTKUYosji5tUreMwTZGN84hBb0XDhB9ouKXRsqkXHq")
                               #^^Consumer Key^^           #^^Consumer Secret^^
    
    #sets the appliction access keys to my consumer key.
    auth.set_access_token("188453340-AsHcJSD3pCo2s4Ya6rOjJYXlW2ZiMARVa0xX8scY", "EQGTXpt507XS42sRTHs4son7bBc0UHhilaDoggfRW8KpZ")
                          #^^Access Token^^                                     #^^Access Token Secret^^
    
    #sends api keys to authenticator and returns access operator to the var api.
    api = tweepy.API(auth)

    #tries to access the api and returns it is working if it does
    try:
        redirect_url = auth.get_authorization_url()
        if (redirect_url != None):
            print("API WORKING!")
            
    #shows no access to api if try doesnt work.
    except:
        print("Authentication Failed!")

    #returns the api operator var
    return api
