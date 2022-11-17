from creational_patterns.factory_method.controllers.Enum.enums import TypeBicycle
from creational_patterns.factory_method.controllers.generic_factory.generic_factory import GenericFactory
from creational_patterns.factory_method.controllers.mountain_factory.mountain_factory import MountainFactory


class BicycleFactory:

    def __init__(self, type_bicycle: TypeBicycle):
        self.type_bicycle = type_bicycle
        self.factories = {
            'mountain_factory': MountainFactory,
            'generic_factory': GenericFactory
        }

    def create_bicycle(self):
        create = self.factories.get(self.type_bicycle.value)
        name, tires, frame = create().description()
        return name, tires, frame
