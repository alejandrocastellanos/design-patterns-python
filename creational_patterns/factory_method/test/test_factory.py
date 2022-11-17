from creational_patterns.factory_method.controllers.Enum.enums import TypeBicycle
from creational_patterns.factory_method.controllers.factory import BicycleFactory


def test_factory():
    bicycle_factory = BicycleFactory(TypeBicycle.GENERIC)
    name, tires, frame = bicycle_factory.create_bicycle()
    assert name == 'Generic Bicycle'
    assert tires == 'Tire size: 15'
    assert frame == 'Frame shape: All terrain'
