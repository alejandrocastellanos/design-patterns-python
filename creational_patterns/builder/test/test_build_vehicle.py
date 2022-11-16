from builder.controllers.builder.builder import Builder
from builder.controllers.director.jeep_builder import JeepBuilder


def test_build_vehicle():
    builder = Builder()
    director_jeep = JeepBuilder()

    director_jeep.set_builder(builder)
    jeep = director_jeep.create_jeep()
    body, engine, tire = jeep.vehicle_description()

    assert engine == 'Engine: 1200'
    assert body == 'Body: PICKUP'
    assert tire == 'Tire size: 30'
