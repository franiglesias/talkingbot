#!/usr/bin/python
# -*- coding: utf-8 -*-

# References
# ==========
# https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app
# https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
# https://github.com/xurxof/twttrBadPython
import time

from tweepy import TweepError

from configuration import Configuration
from feedreader import FeedReader
from getfromfeed import GetFromFeed
from twitter import Twitter


class Bot:
    def __init__(self, twitter, source):
        self.twitter = twitter
        self.source = source

    def say(self):
        message = self.source.get_message()
        print message
        self.twitter.update_status(message)

    def listen(self, term):
        tweets = self.twitter.get_tweets(term)
        if tweets is None:
            print 'Nothing to report!'
            return
        for tweet in tweets:
            print tweet.text
            self.say()


if __name__ == "__main__":
    try:
        while True:
            bot = Bot(
                Twitter(Configuration('conf.yml')),
                GetFromFeed(FeedReader('http://franiglesias.github.io/feed.xml'))
            )
            if bot.listen('@BotTalking'):
                bot.say()
            time.sleep(10)
    except TweepError as something_wrong:
        print something_wrong[0][0]['message']
        exit(-1)
