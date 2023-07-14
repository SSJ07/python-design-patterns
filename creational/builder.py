"""
Builder design pattern is creational pattern.
It used to build complex object step by step.
"""


class Car:
    def __init__(self):
        self.brand = None
        self.color = None
        self.engine = None

    def __str__(self):
        return f"{self.brand} : {self.color} : {self.engine}"


class CarBuilder:

    def __init__(self):
        self.car = Car()

    def set_brand(self, brand: str) -> None:
        self.car.brand = brand

    def set_color(self, color) -> None:
        self.car.color = color

    def set_engine(self, engine: str) -> None:
        self.car.engine = engine

    def build(self) -> Car:
        return self.car


def main():
    car_builder = CarBuilder()
    car_builder.set_brand("Ferrari")
    car_builder.set_color("Black")
    car_builder.set_engine("450CC")

    car = car_builder.build()

    print("Car constructed successfully: ", car)


if __name__ == '__main__':
    main()
