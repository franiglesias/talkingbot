#!/usr/bin/python
# -*- coding: utf-8 -*-

# References
# ==========
# https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app
# https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
# https://github.com/xurxof/twttrBadPython

from tweepy import TweepError

from configuration import Configuration
from twitter import Twitter
from getfromfeed import GetFromFeed


class TalkingBot:
    def __init__(self, twitter, source):
        self.twitter = twitter
        self.source = source

    def say(self):
        self.twitter.get_api().update_status(status=self.source.get_message())


if __name__ == "__main__":
    try:
        bot = TalkingBot(
            Twitter(Configuration('conf.yml')),
            GetFromFeed('https://franiglesias.github.io/feed.xml')
        )
        bot.say()
    except TweepError as something_wrong:
        print something_wrong[0][0]['message']
        exit(-1)
