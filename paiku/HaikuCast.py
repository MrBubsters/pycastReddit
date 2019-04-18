#! usr/bin/python3
import argparse
import configparser
import time
import praw
import pychromecast
from pychromecast.controllers.youtube import YouTubeController


def input_args():
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
    return args


def get_data(count):
    postDict = {'title': [], 'body': [], 'score': [], 'created': [], 'id': [], 'url': [], 'comm_count': []}

    config = configparser.ConfigParser()
    config.read('config.ini')
    reddit = praw.Reddit(client_id=config['PRAW']['client_id'], \
                         client_secret=config['PRAW']['client_secret'], \
                         user_agent=config['PRAW']['user_agent'], \
                         username=config['PRAW']['username'], \
                         password=config['PRAW']['password'])

    subreddit = reddit.subreddit(args.subreddit)
    for submission in subreddit.hot(limit = count):
        postDict['title'].append(submission.title)
        postDict['url'].append(submission.url)
    return postDict


def get_ID(link):
    id = link[-11:]
    return id


def cast(postDict):
    i = 1
    chromecasts = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == args.cast)
    cast.wait()
    yt = YouTubeController()
    for value in postDict['url']:
        cast.register_handler(yt)
        video = get_ID(postDict['url'][i])
        if not (yt._screen_id and yt._session):
            yt.play_video(video)
            print('Casting: ' + postDict['title'][i])

        else:
            yt.add_to_queue(video)
            print('Queueing: ' + postDict['title'][i])

        i += 1
        time.sleep(5)


if __name__ == '__main__':
    args = input_args()
    cast(get_data(args.count))
