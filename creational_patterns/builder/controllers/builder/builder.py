from builder.controllers.parts.body import Body
from builder.controllers.parts.engine import Engine
from builder.controllers.parts.wheel import Wheel
from builder.controllers.vehicle import Vehicle


class Builder:

    def __init__(self):
        self.size = None
        self.horse_power = None
        self.shape = None

    def set_wheel_parameters(self, size):
        self.size = size
        return self

    def set_engine_parameters(self, horse_power):
        self.horse_power = horse_power
        return self

    def set_body_parameters(self, shape):
        self.shape = shape
        return self

    def build(self):
        wheel = Wheel(self.size)
        engine = Engine(self.horse_power)
        body = Body(self.shape)
        vehicle = Vehicle()
        vehicle.set_body(body)
        vehicle.set_engine(engine)
        vehicle.attach_wheel(wheel)
        return vehicle
