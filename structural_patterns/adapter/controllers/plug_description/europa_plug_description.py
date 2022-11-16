from adapter.controllers.adapter.adapter import Adapter
from adapter.controllers.vehicle_type.europa import Europa


class EuropaPlugDescription:

    def __init__(self):
        self.europa_plug = Europa()

    def description(self):
        adapter = Adapter(self.europa_plug, type=self.europa_plug.plug_b())
        return adapter.name, adapter.type
