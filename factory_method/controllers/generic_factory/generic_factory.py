from factory_method.controllers.base_factory import BaseFactory
from factory_method.controllers.generic_factory.generic_frame import GenericFrame
from factory_method.controllers.generic_factory.generic_tire import GenericTire


class GenericFactory(BaseFactory):

    def __init__(self):
        super().__init__()
        self.name = 'Generic Bicycle'

    def add_tires(self):
        return GenericTire().type_tire(15)

    def add_frame(self):
        return GenericFrame().type_frame('All terrain')
