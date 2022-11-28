from abc import ABC, abstractmethod


class MakeMeal(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def go(self):
        return self.prepare(), self.cook(), self.eat()
