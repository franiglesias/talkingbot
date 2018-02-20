#!/usr/bin/python
# -*- coding: utf-8 -*-

# References
# ==========
# https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app
# https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python


import yaml
import tweepy


class Twitter:
    def __init__(self):
        configuration = self.load_credentials()

        self.access_token_secret = configuration['twitter']['access_token_secret']
        self.access_token = configuration['twitter']['access_token']
        self.consumer_secret = configuration['twitter']['consumer_secret']
        self.consumer_key = configuration['twitter']['consumer_key']

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

    def say(self, aTweet):
        self.api.update_status(status=aTweet)


# Write a tweet to push to our Twitter account
tweet = 'Just cleaning!'
twitter = Twitter()
twitter.say(tweet)
