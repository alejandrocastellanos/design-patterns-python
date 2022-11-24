from behavioral_patterns.chain_of_responsability.controllers.abstract_handler import AbstractHandler


class SecondConcreteHandler(AbstractHandler):

    def apply_payment(self, value):
        # fee
        if value > 0:
            return value - 15
