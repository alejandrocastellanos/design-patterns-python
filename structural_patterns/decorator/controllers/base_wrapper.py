from abc import ABC, abstractmethod


class BaseWrapper(ABC):

    def __init__(self, wrapper):
        self._wrapper = wrapper

    @abstractmethod
    def render(self):
        # define de logic
        pass
