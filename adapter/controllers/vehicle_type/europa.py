from adapter.controllers.vehicle_type.base import Base


class Europa(Base):

    def __init__(self):
        super().__init__()
        self.name = "Europa"

    def plug_b(self):
        return "Plug b type"
