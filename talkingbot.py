#!/usr/bin/python
# -*- coding: utf-8 -*-

# References
# ==========
# https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app
# https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
# https://github.com/xurxof/twttrBadPython

import yaml
import tweepy

from getfromfeed import GetFromFeed


class TalkingBot:
    def __init__(self, source):
        self.source = source
        configuration = self.load_credentials()

        self.access_token_secret = configuration['twitter']['access_token_secret']
        self.access_token = configuration['twitter']['access_token']
        self.consumer_secret = configuration['twitter']['consumer_secret']
        self.consumer_key = configuration['twitter']['consumer_key']
        self.me = configuration['twitter']['bot']
        self.api = self.get_api()

    def load_credentials(self):
        with open("conf.yml", 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)

    def say(self):
        self.api.update_status(status=self.source.get_message())


if __name__ == "__main__":
    try:
        bot = TalkingBot(GetFromFeed('https://franiglesias.github.io/feed.xml'))
        bot.say()
    except tweepy.TweepError as something_wrong:
        print something_wrong[0][0]['message']
        exit(-1)

