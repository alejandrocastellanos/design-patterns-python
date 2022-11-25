from abc import ABC, abstractmethod


class State(ABC):

    def __init__(self):
        self._elevator = None

    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, elevator):
        self._elevator = elevator

    @abstractmethod
    def push_down_button(self):
        pass

    @abstractmethod
    def push_up_button(self):
        pass
