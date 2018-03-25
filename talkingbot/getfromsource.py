from abc import ABCMeta, abstractmethod


class GetFromSource(object):
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def get_message(self):
        pass
