from observer.controllers.subscriber.base import Subscriber


class AlejoSubscriber(Subscriber):

    def __init__(self):
        super().__init__(name='Alice')

    def update(self, message):
        return print(f'{self.name} got message "{message}" and other Alejo things')
