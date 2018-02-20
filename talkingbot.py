#!/usr/bin/python
# -*- coding: utf-8 -*-

import yaml
import tweepy


class Twitter:
    def __init__(self):
        self.load_credentials()
        self.api = self.get_api()

    def load_credentials(self):
        with open("conf.yml", 'r') as stream:
            try:
                configuration = yaml.load(stream)
                self.consumer_key = configuration['twitter']['consumer_key']
                self.consumer_secret = configuration['twitter']['consumer_secret']
                self.access_token = configuration['twitter']['access_token']
                self.access_token_secret = configuration['twitter']['access_token_secret']
            except yaml.YAMLError as exc:
                print(exc)

    def get_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)

    def say(self, aTweet):
        self.api.update_status(status=aTweet)


# Write a tweet to push to our Twitter account
tweet = 'This has a link http://franiglesias.github.io'
twitter = Twitter()
twitter.say(tweet)
