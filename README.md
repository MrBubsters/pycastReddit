# PycastReddit

This simple script pulls youtube data from the front page of any subreddit. 
The script was made to be used mainly for casting /r/YoutubeHaiku but will work with any subreddit where posts are youtube links. 

## Getting Started

Before you can run anything, in order to allow PRAW to pull reddit posts, you will need to setup a new reddit app. 
More information on configuring PRAW can be found on the quick start page https://praw.readthedocs.io/en/latest/getting_started/quick_start.html

Once you have registered a new application for the Reddit API, PRAW will need 5 fields filled out that can be found in config.ini

* client_id
* client_secret
* user_agent
* username
* password


### Prerequisites

All of the dependencies are listed in requirements.txt and can be installed with the following command:

```
pip3 install -r requirements.txt
```

## Running the script

The command line interface accepts 3 arguments
* --subreddit or -s
* --count or -n
* --cast or -c
### Command line interface

Running this command would pull the top 15 posts from /r/YoutubeHaiku and cast it to 'LivingRoom' cast device on the same network
```
python3 HaikuCast.py -s YoutubeHaiku -n 15 -c LivingRoom
```

## Built With

* [pychromecast](https://github.com/balloob/pychromecast) - chromecast library for python3

## Authors

* **Chris Kuehn** - *Initial work* - [MrBubsters](https://github.com/MrBubsters)

## Acknowledgments

* Credit goes to baloob for creating a python wrapper for chromecasts that is the base for this project
