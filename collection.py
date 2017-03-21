import got3
import tweepy

from locGet import geo

class collection:
    def __init__(self, api, db):
        self.api = api
        self.db = db

    #gets tweets from hashtag "#brexit" and puts them in the mongo database
    def getTweets(self, hashtag):

        self.tweetCriteria = got3.manager.TweetCriteria().setQuerySearch(
            hashtag).setSince("2016-06-12").setUntil("2016-06-13").setMaxTweets(1)
        self.brexitTweets = got3.manager.TweetManager.getTweets(
            self.tweetCriteria)

        # brexitTweets =
        # tweepy.Cursor(api.search,q="#brexit",show_user=True,locale=True,wait_on_rate_limit=True).items()

        #loops through the list of tweets
        for self.tweets in self.brexitTweets:

            self.out = self.tweets.text
            self.name = self.tweets.username
            self.uid = self.tweets.id
            self.date = self.tweets.date
            self.geo = geo().locFind(self.name)
            self.followers = []
            self.friends = []
            self.tmp = 0

            #gets the users followers id and puts them in a list
            for self.followersID in tweepy.Cursor(self.api.followers_ids, screen_name=self.name, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items(100):
                #print ("Adding to followers list: ",users)
                self.followers.append(self.followersID)

            #gets the users following and puts them in the list
            for self.followingID in tweepy.Cursor(self.api.friends_ids, screen_name=self.name, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items(100):
                #print ("Adding to friends list: ",users.screen_name)
                self.friends.append(self.followingID)

            #shows what is being added to the database
            print("\n\nAdded:", "\n    Username:", self.name.encode("utf-8"), "\n    User ID:", self.uid, "\n    Date:", self.date, "\n    Location:", self.geo.encode("utf-8"),
                  "\n    Followers:", self.followers, "\n    Following:", self.friends, "\n    Tweets:", self.out.encode("utf-8"))  # shows tweets being added to the DB

            #adds the data to the database
            self.results = self.db.tweets.insert_one(
                {
                    "username": self.name,
                    "userID": self.uid,
                    "date": self.date,
                    "location:": self.geo,
                    "followers": self.followers,
                    "friends": self.friends,
                    "tweet": self.out
                }
            )
