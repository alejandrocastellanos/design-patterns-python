from abc import ABC, abstractmethod


class BaseComponent(ABC):

    #  compose objects into tree structures

    @abstractmethod
    def get_size(self):
        # returns size of the component in mb
        pass
