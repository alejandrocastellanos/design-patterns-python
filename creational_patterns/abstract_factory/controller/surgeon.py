from .instrumentalist import Instrumentalist


class Surgeon:

    def __init__(self, instrumentalist: Instrumentalist):
        self._instrumentalist = instrumentalist

    def operate(self):
        cutting_tool = self._instrumentalist.cutting_tool
        drying_tool = self._instrumentalist.drying_tool
        return f'Operating with {cutting_tool} and {drying_tool}'
