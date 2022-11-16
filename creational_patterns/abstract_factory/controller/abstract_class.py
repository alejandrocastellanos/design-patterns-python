from abc import ABC, abstractmethod


class AbstractTool(ABC):

    @abstractmethod
    def create_cutting_tool(self):
        pass

    @abstractmethod
    def create_dying_tool(self):
        pass
