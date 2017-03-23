import got3

tweetCriteria = got3.manager.TweetCriteria().setQuerySearch('twitter').setSince("2017-02-02").setUntil("2017-02-03").setMaxTweets(1)
tweet = got3.manager.TweetManager.getTweets(tweetCriteria)[0]

print("id:", tweet.author_id)
print("username:",tweet.username)
