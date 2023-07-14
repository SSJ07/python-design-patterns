"""
@author : Shrikant Jagtap

Use Case of Factory method pattern:
    -> Difficult to track object creation in various places in your application
    -> Factory methods allows to centralize object creations in one place and provide it throughout the app

Factory method pattern:
    1. It creates conditional objects for given input.
"""
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def draw(self):
        print("Drawing Rectangle.")


class Circle(Shape):

    def draw(self):
        print("Drawing Circle")


class Square(Shape):
    def draw(self):
        print("Drawing square")


class ShapeFactory:

    @staticmethod
    def create_shape(shape: str) -> Shape:
        if not isinstance(shape, str):
            raise Exception(f"Shape name should in string format: got {type(shape)}")
        if shape.lower() == "rectangle":
            return Rectangle()
        elif shape.lower() == "circle":
            return Circle()
        elif shape.lower() == "square":
            return Square()
        else:
            raise Exception("No suitable Shape found!")


def main():
    shape = ShapeFactory.create_shape("circle")
    shape.draw()

    shape = ShapeFactory.create_shape("square")
    shape.draw()

    shape = ShapeFactory.create_shape("rectangle")
    shape.draw()

    ShapeFactory.create_shape("not shape")


if __name__ == '__main__':
    main()
