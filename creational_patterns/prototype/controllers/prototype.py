import copy
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):

    def __init__(self):
        self._id = None
        self._type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self._type

    def get_id(self):
        return self._id

    def set_id(self, sid):
        self._id = sid

    def clone(self):
        return copy.copy(self)
