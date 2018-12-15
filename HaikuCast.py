#! usr/bin/python3
import argparse
import praw
import time
import pychromecast.pychromecast as pychromecast
from pychromecast.pychromecast.controllers.youtube import YouTubeController
import configparser
import os

parser = argparse.ArgumentParser()
parser.add_argument('--subreddit', '-s', help="Subreddit to pull videos from. Must be video only posts", type= str)
parser.add_argument('--count', '-n', help="Number of posts to pull", type= int)
parser.add_argument('--cast', '-c', help="Name of chromecast", type= str)


args = parser.parse_args()
print(args)
if (args.subreddit == None) :
    print("No subreddit defined")
    exit()
if (args.count == None) :
    print("No post count defined")
    exit()
if (args.cast == None) :
    print("No cast device defined")
    exit()


postDict = {'title':[], 'body':[], 'score':[], 'created':[], 'id':[], 'url':[], 'comm_count':[]}

config = configparser.ConfigParser()
config.read('config.ini')
reddit = praw.Reddit(client_id=config['PRAW']['client_id'], \
                     client_secret=config['PRAW']['client_secret'], \
                     user_agent=config['PRAW']['user_agent'], \
                     username=config['PRAW']['username'], \
                     password=config['PRAW']['password'])

def getData(count):

    subreddit = reddit.subreddit(args.subreddit)
    for submission in subreddit.hot(limit = count):
        postDict['title'].append(submission.title)
        postDict['url'].append(submission.url)

def getID(link):
    id = link[-11:]
    return id


def castData():
    i = 1
    chromecasts = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == args.cast)
    cast.wait()
    yt = YouTubeController()
    for value in postDict['url']:
        cast.register_handler(yt)
        video = getID(postDict['url'][i])
        if not (yt._screen_id and yt._session):
            yt.play_video(video)
            print('Casting: ' + postDict['title'][i])

        else:
            yt.add_to_queue(video)
            print('Queueing: ' + postDict['title'][i])

        i += 1
        time.sleep(5)

#print("Enter command -s \"subreddit\" -p post count -c \"cast name\"")

getData(args.count)
#castSetup()
castData()