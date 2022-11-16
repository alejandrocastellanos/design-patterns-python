from .abstract_class import AbstractTool


class InstrumentalistInJungle(AbstractTool):

    def create_cutting_tool(self):
        return 'Knife'

    def create_dying_tool(self):
        return 'Rag'
