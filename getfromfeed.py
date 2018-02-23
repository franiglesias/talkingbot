#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import feedparser


# References
# ==========
# http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python
# https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20

class GetFromFeed:
    def __init__(self, feed_url):
        self.feed = feedparser.parse(feed_url)
        pass

    def get_message(self):
        entry = random.choice(self.feed.entries)
        message = '{} {}'.format(entry.title.encode('utf-8'), entry.link.encode('utf-8'))
        print 'Trying to tweet: {}'.format(message)
        return message

