import tweepy
def authentigate():

    auth = tweepy.OAuthHandler("esOD1d4qKPys3fjwFrrMxevGv", "ClhLgKumBTKUYosji5tUreMwTZGN84hBb0XDhB9ouKXRsqkXHq")
    auth.set_access_token("188453340-AsHcJSD3pCo2s4Ya6rOjJYXlW2ZiMARVa0xX8scY", "EQGTXpt507XS42sRTHs4son7bBc0UHhilaDoggfRW8KpZ")

    api = tweepy.API(auth)

    try:
        redirect_url = auth.get_authorization_url()
        print("API WORKING!")
    except:
        print("Authentication Failed!")

    return api
