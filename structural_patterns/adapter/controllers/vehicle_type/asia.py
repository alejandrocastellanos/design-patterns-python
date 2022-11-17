from structural_patterns.adapter.controllers.vehicle_type.base import Base


class Asia(Base):

    def __init__(self):
        super().__init__()
        self.name = "Motorcycle"

    def plug_c(self):
        return "Eight Wheeler"
