from creational_patterns.factory_method.controllers.base_factory import BaseFactory
from creational_patterns.factory_method.controllers.generic_factory.generic_frame import GenericFrame
from creational_patterns.factory_method.controllers.generic_factory.generic_tire import GenericTire


class MountainFactory(BaseFactory):

    def __init__(self):
        super().__init__()
        self.name = 'Mountain Bicycle'

    def add_tires(self):
        return GenericTire().type_tire(30)

    def add_frame(self):
        return GenericFrame().type_frame('Mountain terrain')
