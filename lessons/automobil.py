class Car:
    def __init__(self, model, year, volume_engine, price, mileage, wheels):
        self.model = model
        self.year = year
        self.volume_engine = volume_engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def car_description(self):
        description = (f"Модель: {self.model}, "
                       f"год выпуска: {self.year}, "
                       f"объем двигателя: {self.volume_engine}, "
                       f"цена: {self.price}, "
                       f"пробег: {self.mileage}, "
                       f"кол-во колес: {self.wheels}")
        return description


class Truck(Car):
    def __init__(self, model, year, volume_engine, price, mileage, wheels):
        super().__init__(model, year, volume_engine, price, mileage, wheels)

    def update_wheels(self, wheels):
        self.wheels = wheels


car = Car('Tesla', 2023, 2000, 7000000, 1000, 4)
print(car.car_description())

truck = Truck('Volvo truck', 2024, 6000, 12000000, 0, 8)
truck.update_wheels(8)
print(truck.car_description())
