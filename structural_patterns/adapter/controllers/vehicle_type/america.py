from structural_patterns.adapter.controllers.vehicle_type.base import Base


class America(Base):

    def __init__(self):
        super().__init__()
        self.name = "America"

    def plug_a(self):
        return "Plug A type"
