from structural_patterns.flyweight.controllers.complex_cars import ComplexCars


class CarFamilies:

    car_family = {}
    
    def __new__(cls, name, car_family_id):
        try:
            id = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.car_family[car_family_id] = id
        return id

    def set_car_info(self, car_info):
        complex_car = ComplexCars()
        self.car_info = complex_car.cars(car_info)

    def get_car_info(self):
        return (self.car_info)
