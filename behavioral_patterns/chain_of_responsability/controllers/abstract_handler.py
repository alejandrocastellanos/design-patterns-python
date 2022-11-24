from abc import abstractmethod, ABC


class AbstractHandler(ABC):

    def __init__(self, nxt):
        self._next = nxt

    def handle(self, payment):
        _payment_applied = self.apply_payment(payment)
        if self._next:
            return self._next.handle(_payment_applied)
        return _payment_applied

    @abstractmethod
    def apply_payment(self, payment):
        # redefine the applu payment
        pass
