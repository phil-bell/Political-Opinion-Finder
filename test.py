
# import got3

# tweetCriteria = got3.manager.TweetCriteria().setQuerySearch('twitter').setSince("2017-02-02").setUntil("2017-02-03").setMaxTweets(1)
# tweet = got3.manager.TweetManager.getTweets(tweetCriteria)[0]

# print("id:", tweet.author_id)
# print("username:",tweet.username)
# from time import sleep
# import codecs
# import threading
# stopper = True

# def spinner():
#     global stopper
#     while stopper == True:
#         print("Analysing [/]", end="\r")
#         sleep(.1)
#         print("Analysing [—]", end="\r")
#         sleep(.1)
#         print("Analysing [\]", end="\r")
#         sleep(.1)
#         print("Analysing [|]", end="\r")
#         sleep(.1)
# def stop():
#     global stopper
#     sleep(5)
#     stopper = False

# threading.Thread(target=test,args=()).start()
# threading.Thread(target=stop, args=()).start()

# import nltk
# nltk.download()

from sentiment import sent

print(sent.ment("I really love it when this happens"))
