from .abstract_class import AbstractTool


class InstrumentalistInOperatingRoom(AbstractTool):

    def create_cutting_tool(self):
        return 'Scalpel'

    def create_dying_tool(self):
        return 'Compress'
