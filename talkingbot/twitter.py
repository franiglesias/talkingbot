#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy


class Twitter:
    def __init__(self, configuration):
        self.access_token_secret = configuration.get_access_token_secret()
        self.access_token = configuration.get_access_token()
        self.consumer_secret = configuration.get_consumer_secret()
        self.consumer_key = configuration.get_consumer_key()

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(auth)

    def get_api(self):
        return self.api

    def update_status(self, message):
        self.get_api().update_status(status=message)
