#!/usr/bin/python
# -*- coding: utf-8 -*-

import yaml


class Configuration:
    def __init__(self, path):
        self.data = self.load_from(path)

    @staticmethod
    def load_from(path):
        with open(path, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_access_token(self):
        return self.data['twitter']['access_token']

    def get_access_token_secret(self):
        return self.data['twitter']['access_token_secret']

    def get_consumer_secret(self):
        return self.data['twitter']['consumer_secret']

    def get_consumer_key(self):
        return self.data['twitter']['consumer_key']
