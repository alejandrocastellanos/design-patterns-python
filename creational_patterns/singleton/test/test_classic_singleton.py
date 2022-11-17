from creational_patterns.singleton.controller.classic_singleton import DBClassicSingleton


def test_instance_classic_singleton():
    connection_one = DBClassicSingleton()
    connection_two = DBClassicSingleton()

    print('connection_one', connection_one)
    print('connection_two', connection_one)

    assert connection_one == connection_two

# pytest -s -vv
