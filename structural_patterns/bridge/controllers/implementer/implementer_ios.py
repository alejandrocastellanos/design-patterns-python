from abc import ABCMeta, abstractmethod


class IOsImplementer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def operate_implement():
        # will be overridden in implementer
        pass
