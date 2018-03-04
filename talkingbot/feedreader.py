import random

import feedparser


class FeedReader:
    def __init__(self, url):
        self.url = url
        self.entries = self.refresh()
        pass

    def refresh(self):
        feed = feedparser.parse(self.url)
        return feed.entries

    def getRandom(self):
        return random.choice(self.entries)
