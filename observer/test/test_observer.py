from observer.controllers.publisher import Publisher
from observer.controllers.subscriber.alejo_subscriber import AlejoSubscriber
from observer.controllers.subscriber.alice_subscriber import AliceSubscriber
from observer.controllers.subscriber.bob_subscriber import BobSubscriber


def test_observer():
    pub = Publisher()
    pub.register(BobSubscriber())
    pub.register(AlejoSubscriber())
    pub.register(AliceSubscriber())

    pub.dispatch('It is lunchtime!')

