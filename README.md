# Political Opinion Finder

This is my 3rd year Dissertation project. It involves a program that collects Tweets from twitter, analyses them to evaluate there opinion and then compare the overall opinion to pollster data.

## Motivation

The motivation of this project is to investigate into the difference between political opnions shared on online social media to the opinions of the general populace (opinions gathered from pollsters).

## Installation

Clone the repositary then install the following Python libraries:
* `Tweepy Twitter API library for accessing Twitter
* `pymongo MongoDB library for using MongoDB
* `codecs Encoding library for 

At this current stage in development the program requires a local MongoDB to be active (Please install from [MongoDB](https://www.mongodb.com/download-center?jmp=nav))

User must also create a JSON file with there [Twitter API](https://apps.twitter.com/) credentials, use the [example](https://github.com/philhabell/Political-Opinion-Finder/blob/master/apiCredentialsExample.json) file as a guide.

## Operation

Simple run:
``` 
python ./main.py
```

## Licence
Copyright (C) 2017 Philip Bell - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Philip Bell <philhabell@gmail.com>, March 2017

