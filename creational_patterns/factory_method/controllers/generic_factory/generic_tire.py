from creational_patterns.factory_method.controllers.base_part_type import BasePartType


class GenericTire(BasePartType):

    def type_tire(self, size):
        return f'Tire size: {size}'
