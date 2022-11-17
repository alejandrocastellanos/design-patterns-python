from creational_patterns.factory_method.controllers.generic_factory.generic_factory import GenericFactory
from creational_patterns.factory_method.controllers.mountain_factory.mountain_factory import MountainFactory


def test_generic_bicycle_factory():
    generic_factory = GenericFactory()
    name, tires, frame = generic_factory.description()
    assert name == 'Generic Bicycle'
    assert tires == 'Tire size: 15'
    assert frame == 'Frame shape: All terrain'


def test_mountain_bicycle_factory():
    generic_factory = MountainFactory()
    name, tires, frame = generic_factory.description()
    assert name == 'Mountain Bicycle'
    assert tires == 'Tire size: 30'
    assert frame == 'Frame shape: Mountain terrain'
