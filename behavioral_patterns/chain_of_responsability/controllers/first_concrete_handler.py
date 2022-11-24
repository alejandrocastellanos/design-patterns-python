from behavioral_patterns.chain_of_responsability.controllers.abstract_handler import AbstractHandler


class FirstConcreteHandler(AbstractHandler):

    def apply_payment(self, value):
        # taxes 1
        if value > 0:
            return value - 20
