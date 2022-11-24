from behavioral_patterns.chain_of_responsability.controllers.first_concrete_handler import FirstConcreteHandler
from behavioral_patterns.chain_of_responsability.controllers.second_concrete_handler import SecondConcreteHandler
from behavioral_patterns.chain_of_responsability.controllers.third_concrete_handler import ThirdConcreteHandler


class Payment:

    def __init__(self, payment: float):
        self._payment = payment

    def apply_payment(self):
        handle = FirstConcreteHandler(
            nxt=SecondConcreteHandler(
               nxt=ThirdConcreteHandler(
                   nxt=None
               )
            )
        )
        return handle.handle(self._payment)
