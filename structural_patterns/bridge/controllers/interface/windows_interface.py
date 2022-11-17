from structural_patterns.bridge.controllers.interface.base_ios_interface import BaseIosInterface


class Windows(BaseIosInterface):

    def __init__(self, implementer):
        self.implementer = implementer

    def operate(self):
        return self.implementer.operate_implement()
