"""
Flyweight Design Pattern

--> Flyweight design pattern is optimization design pattern.
--> In Object oriented programming, We need to create lots of objects and that can lead memory issue.
--> Flyweight design pattern is a technique used to minimize memory usage and improve performance by introducing
    data sharing between similar objects
--> It is useful to make memory efficient program which creates a huge number of objects

To use flyweight design pattern effectively, needs satisfied following conditions:
    --> The application needs to use a large number of objects
    --> There are so many objects that it's too expensive to store/render them. Once mutable state is removed,
        Many groups of distinct objects can be replaced by relatively few shared objects

Example:
        All embedded systems (phone, tablets, game consoles and so on) and performance critical applications
        like: video games, 3-D graphics processing, real-time systems, and so forth can benefit from it

"""
import random
from enum import Enum
from typing import Dict


class CarType(Enum):
    subcompact = "subcompact"
    compact = "compact"
    suv = "suv"


class Car:

    pool: Dict[str, object] = dict()

    def __new__(cls, car_type: CarType) -> object:
        obj = cls.pool.get(car_type.name)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[car_type.name] = obj
            obj.car_type = car_type.name
        return obj

    def render(self, color: str, x: float, y: float) -> None:
        print(f"Render car type: {self.car_type} with color: {color} at {x}, {y}")


def main():
    rnd = random.Random()
    colors = 'white black silver gray red blue brown beige yellow green'.split()
    min_point, max_point = 0, 100
    car_counter = 0

    for _ in range(10):
        c1 = Car(CarType.subcompact)
        c1.render(rnd.choices(colors), rnd.randint(min_point, max_point), rnd.randint(min_point, max_point))
        car_counter += 1

    for _ in range(3):
        c1 = Car(CarType.compact)
        c1.render(rnd.choices(colors), rnd.randint(min_point, max_point), rnd.randint(min_point, max_point))
        car_counter += 1

    for _ in range(3):
        c1 = Car(CarType.suv)
        c1.render(rnd.choices(colors), rnd.randint(min_point, max_point), rnd.randint(min_point, max_point))
        car_counter += 1

    print(f"Total objects creation are called : {car_counter} times")
    print(f"But only {len(Car.pool.keys())} objects are created : {Car.pool.values()}")


if __name__ == '__main__':
    main()
