from structural_patterns.flyweight.controllers.car_families import CarFamilies


def test_flyweight():
    car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferarri'),('b', 1, 'Audi'))
    car_family_object = []
    for car in car_data:
        obj = CarFamilies(car[0], car[1])
        obj.set_car_info(car[2])
        car_family_object.append(obj)

    id_a_audi = id(car_family_object[0])
    id_a_ferrari = id(car_family_object[1])
    id_b_audi = id(car_family_object[2])

    assert id_a_audi == id_b_audi
    assert id_a_ferrari != id_a_audi
    assert car_family_object[0].get_car_info() == 'ComplexPattern Audi'
