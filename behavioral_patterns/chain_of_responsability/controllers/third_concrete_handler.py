from behavioral_patterns.chain_of_responsability.controllers.abstract_handler import AbstractHandler


class ThirdConcreteHandler(AbstractHandler):

    def apply_payment(self, value):
        # taxes 2
        if value > 0:
            return value - 5
