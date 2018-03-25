#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import tweepy

LAST_TWEET_FILE = "lastTweet.txt"


class Twitter:
    def __init__(self, configuration):
        self.access_token_secret = configuration.get_access_token_secret()
        self.access_token = configuration.get_access_token()
        self.consumer_secret = configuration.get_consumer_secret()
        self.consumer_key = configuration.get_consumer_key()
        self.retrieve_last_id()
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(auth)

    def get_api(self):
        return self.api

    def update_status(self, message):
        self.get_api().update_status(status=message)

    def get_tweets(self, term):
        print "Getting last tweets for me."
        tweets = self.get_api().search(q=term, since_id=self.last_id)
        if not tweets:
            print 'No one talks to me :-(.'
            return None
        for tweet in tweets:
            print 'Hey, someone is talking to me :-).'
            if tweet.id > self.last_id:
                self.last_id = tweet.id
        self.persist_last_id(self.last_id)
        return tweets

    def persist_last_id(self, id):
        file = open(LAST_TWEET_FILE, "w")
        file.write(str(id))
        file.close()

    def retrieve_last_id(self):
        if os.path.isfile(LAST_TWEET_FILE):
            file = open(LAST_TWEET_FILE, "r")
            self.last_id = int(file.readline())
            file.close()
        else:
            self.last_id = 0
