from .instrumentalist_in_jungle import InstrumentalistInJungle
from .instrumentalist_in_operating_room import InstrumentalistInOperatingRoom


class Instrumentalist:

    def __init__(self, location):
        self._location = location
        self._factory_tools = None

    def select_tools(self):
        location = {
            'jungle': InstrumentalistInJungle,
            'operating room': InstrumentalistInOperatingRoom
        }
        set_location = location.get(self._location)
        assert set_location, 'Location not parameterized'
        self._factory_tools = set_location()

    @property
    def cutting_tool(self):
        return self._factory_tools.create_cutting_tool()

    @property
    def drying_tool(self):
        return self._factory_tools.create_dying_tool()
