# Political Opinion Finder

This is my 3rd year BSc Computer Science Degree Dissertation project. It involves a program that collects Tweets from twitter, analyses them using natural language to calculate their political opinion so it can then be compared general populace opinions from pollster data.

## Motivation

The motivation of this project is to investigate into the difference between political opinions shared on online social media to the opinions of the general populace (opinions gathered from [pollsters data](https://github.com/philhabell/Political-Opinion-Finder/blob/master/data/polls.json)) by using natural language and big data analyse.

## Findings

The findings of the investigation can be found in the paper I wrote on [Academia](https://www.academia.edu/32934838/Do_the_political_opinions_shared_on_Social_Media_platform_Twitter_accurately_represent_the_political_opinions_of_the_general_populace). The TLDR was that majority of Twitter users did side with remain. I go into further detail on why in the paper.

## Installation

Clone the repo, install [Python 3](https://www.python.org/downloads/) and the following Python libraries using `pip install`:
* `Tweepy` Twitter API library for accessing Twitter
* `pymongo` MongoDB library for using MongoDB
* `codecs` Encoding library for encoding the tweets
* `nltk` Natural language library for analysing meaning of tweets
* `tqdm`

Install the following from their `.whl` from the [Windows Binary](http://www.lfd.uci.edu/~gohlke/pythonlibs/) site using `pip install`:
* `numpy`
* `scipy`
* `scit_learn`
* `sklearn`

This is for Windows(I believe they work with normal `pip install` on Linux).

Create a JSON file with users MongoDB server credentials, use the [example](https://github.com/philhabell/Political-Opinion-Finder/blob/master/credentials/mongoCredentialsExample.json) file as a guide. If using a local server download [MongoDB](https://www.mongodb.com/download-center?jmp=nav) and leave `mongoURL` empty in the JSON file.

User must also create a JSON file with there [Twitter API](https://apps.twitter.com/) credentials, use the [example](https://github.com/philhabell/Political-Opinion-Finder/blob/master/credentials/apiCredentialsExample.json) file as a guide.


## Operation

Run the following in console/terminal:
``` 
python ./main.py
```
Then select what you would like to do from the menu presented to you.

On first run the program will download the necessary [NLTK data](http://www.nltk.org/data.html) (This may take some time).
It is advised to use `Gather tweets` option on first run so there are tweets in the database.
The calculation of twitter vs poll opinion difference does take a long time (can be hours on a slower system).

## Licence
Copyright (C) 2017 Philip Bell - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited.

Proprietary and confidential.

Written by Philip Bell <philhabell@gmail.com>, March 2017.

**[Back to top](#political-opinion-finder)**