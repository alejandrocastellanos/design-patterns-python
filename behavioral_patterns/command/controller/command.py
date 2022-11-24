from abc import abstractmethod, ABC

from behavioral_patterns.command.controller.door import Door
from behavioral_patterns.command.controller.enum import Action


class Command(ABC):

    def __init__(self):
        self.door = Door()
        self.last_action = None

    @abstractmethod
    def execute(self, action: Action):
        pass

    @abstractmethod
    def undo_execute(self):
        pass
