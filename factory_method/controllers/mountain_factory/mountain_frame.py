from factory_method.controllers.base_part_type import BasePartType


class MountainFrame(BasePartType):

    def type_frame(self, shape: str):
        return f'Frame shape: {shape}'
