import time
from abc import ABC, abstractmethod
from typing import List


class Car(ABC):

    @abstractmethod
    def drive(self):
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class Ferrari(Car):
    def drive(self):
        print("Driving Ferrari")


class BMW(Car):
    def drive(self):
        print("Driving BMW")

    def __str__(self) -> str:
        return "BMW"


class Lamborghini(Car):
    def drive(self):
        print("Driving Lamborghini")


class Mercedes(Car):
    def drive(self):
        print("Driving Mercedes")


class CarFactory(ABC):
    @abstractmethod
    def create_sport_car(self):
        pass

    @abstractmethod
    def create_luxury_car(self):
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class FerrariBMWFactory(CarFactory):
    def create_sport_car(self) -> Ferrari:
        return Ferrari()

    def create_luxury_car(self) -> BMW:
        return BMW()


class LamborghiniMercedesFactory(CarFactory):
    def create_sport_car(self) -> Lamborghini:
        return Lamborghini()

    def create_luxury_car(self) -> Mercedes:
        return Mercedes()


class VehicleFactory:

    @staticmethod
    def create_vehicle(car_factories: List[CarFactory]):
        for car_factory in car_factories:
            print(f"{car_factory}: Creating sport car......")
            time.sleep(2)
            sport_car = car_factory.create_sport_car()
            print(f"{car_factory}:  Created sport car: {sport_car}")
            sport_car.drive()

            print(f"{car_factory}: Creating Luxury car......")
            luxury_car = car_factory.create_luxury_car()
            print(f"{car_factory}:  Created Luxury car: {sport_car}")
            luxury_car.drive()


def main():
    VehicleFactory().create_vehicle([FerrariBMWFactory(), LamborghiniMercedesFactory()])


if __name__ == '__main__':
    main()
