from creational_patterns.builder.controllers.parts.body import Body
from creational_patterns.builder.controllers.parts.engine import Engine
from creational_patterns.builder.controllers.parts.wheel import Wheel


class Vehicle:

    def __init__(self):
        self._wheels = None
        self._engine = None
        self._body = None

    def set_body(self, body: Body):
        self._body = body

    def set_engine(self, engine: Engine):
        self._engine = engine

    def attach_wheel(self, wheel: Wheel):
        self._wheels = wheel

    def vehicle_description(self):
        body = f'Body: {self._body.shape}'
        engine = f'Engine: {self._engine.horse_power}'
        tire = f'Tire size: {self._wheels.size}'
        return body, engine, tire
