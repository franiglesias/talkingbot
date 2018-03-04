#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

# References
# ==========
# http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python
# https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20


class GetFromFeed:
    def __init__(self, reader):
        self.reader = reader

    def get_message(self):
        entry = self.reader.getRandom()
        entry = self.ensure_links_to_first_article_in_series(entry)
        return self.basic_message(entry)

    @staticmethod
    def basic_message(entry):
        return '{} {}'.format(entry.title.encode('utf-8'), entry.link.encode('utf-8'))

    @staticmethod
    def ensure_links_to_first_article_in_series(entry):
        entry.link = re.sub('\d+$', '1', entry.link)
        return entry

