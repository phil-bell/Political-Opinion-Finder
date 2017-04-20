# Political Opinion Finder

This is my 3rd year BSc Computer Science Degree Dissertation project. It involves a program that collects Tweets from twitter, analyses them using natual language to calcualte their political opinion so it can then be compared general populace opinions from pollster data.

## Motivation

The motivation of this project is to investigate into the difference between political opnions shared on online social media to the opinions of the general populace (opinions gathered from [pollsters data](https://github.com/philhabell/Political-Opinion-Finder/blob/master/data/polls.json)) by using natural language and big data analyse.

## Installation

Clone the repositary, install [Python 3](https://www.python.org/downloads/) and the following Python libraries using `pip`:
* `Tweepy` Twitter API library for accessing Twitter
* `pymongo` MongoDB library for using MongoDB
* `codecs` Encoding library for encoding the tweets
* `nltk` Natural language library for analysing meaning of tweets

Install the following from thier `.whl` in the packages folder using `pip`:
* `numpy`
* `scipy`
* `scit_learn`
* `sklearn`

Working version for Windows are not availible on pip(I believe they work on Linux).

Create a JSON file with users MongoDB server credentials, use the [example](https://github.com/philhabell/Political-Opinion-Finder/blob/master/credentials/mongoCredentialsExample.json) file as a guide. If using a local server download [MongoDB](https://www.mongodb.com/download-center?jmp=nav) and leave `mongoURL` empty in the JSON file.

User must also create a JSON file with there [Twitter API](https://apps.twitter.com/) credentials, use the [example](https://github.com/philhabell/Political-Opinion-Finder/blob/master/credentials/apiCredentialsExample.json) file as a guide.


## Operation

Run the following in console/terminal:
``` 
python ./main.py
```
Then select what you would like to do from the menu presented to you.

On first run the program will download the necessary [NLTK data](http://www.nltk.org/data.html) (This may take some time).

## Licence
Copyright (C) 2017 Philip Bell - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Philip Bell <philhabell@gmail.com>, March 2017

**[Back to top](#political-opinion-finder)**