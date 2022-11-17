from creational_patterns.factory_method.controllers.base_part_type import BasePartType


class GenericFrame(BasePartType):

    def type_frame(self, shape: str):
        return f'Frame shape: {shape}'
