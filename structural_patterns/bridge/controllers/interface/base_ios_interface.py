from abc import ABCMeta, abstractmethod


class BaseIosInterface(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def operate():
        # will be overridden in implementer
        pass
