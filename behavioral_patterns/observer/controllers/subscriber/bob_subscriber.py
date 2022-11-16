from observer.controllers.subscriber.base import Subscriber


class BobSubscriber(Subscriber):

    def __init__(self):
        super().__init__(name='Bob')

    def update(self, message):
        return print(f'{self.name} got message "{message}" and other Bob things')
