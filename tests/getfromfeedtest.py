from unittest import TestCase, main

from talkingbot.feedreader import FeedReader
from talkingbot.getfromfeed import GetFromFeed


class Entry():
    def __init__(self):
        pass


class FeedReaderStub(FeedReader):
    def __init__(self, url):
        FeedReader.__init__(self, url)
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def refresh(self):
        pass

    def getRandom(self):
        return self.entries[0]


class GetFromFeedTest(TestCase):

    def test_it_returns_a_random_message_from_feed(self):
        entry = self.prepare_entry_with_title_and_link('Title', 'link')

        reader = FeedReaderStub('url')
        reader.add_entry(entry)

        get_from_feed = GetFromFeed(reader)
        self.assertEqual('Title link', get_from_feed.get_message())

    def test_it_creates_a_tweet_with_title_and_link(self):
        entry = self.prepare_entry_with_title_and_link('Title', 'link')

        reader = FeedReaderStub('url')
        reader.add_entry(entry)

        get_from_feed = GetFromFeed(reader)
        self.assertEquals('Title link', get_from_feed.get_message())

    def test_if_we_get_a_link_to_article_in_series_always_return_the_first(self):
        entry = self.prepare_entry_with_title_and_link('Title', 'link-3')

        reader = FeedReaderStub('url')
        reader.add_entry(entry)

        get_from_feed = GetFromFeed(reader)
        self.assertEquals('Title link-1', get_from_feed.get_message())

    def prepare_entry_with_title_and_link(self, title, link):
        entry = Entry()
        entry.title = title
        entry.link = link
        return entry


if __name__ == "__main__":
    main()
