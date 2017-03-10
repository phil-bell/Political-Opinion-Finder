

#gets random tweets as a test
def pubTweets(api):
    publicTweet = api.home_timeline()
    for tweets in publicTweet:
        out = tweets.text
        print (out.decode("utf-8").encode('cp850','replace').decode('cp850'))

    print ("======================================================")
