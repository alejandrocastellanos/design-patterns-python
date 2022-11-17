from creational_patterns.singleton.controller.borg_singleton import BorgSingleton


def test_instance_borg_singleton():
    first_instance = BorgSingleton()
    second_instance = BorgSingleton()
    print('first_instance', first_instance)
    print('second_instance', second_instance)

    first_instance.age = 28

    assert first_instance != second_instance
    assert first_instance.age == second_instance.age
