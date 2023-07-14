"""
Adapter design pattern

Intent:
    -> Adapter design pattern that allows to work with incompatible interfaces to collaborate.
    -> Helps us to make two incompatible interfaces compatible.

Use case:
    -> Let's suppose we have old system, and we want to use it with our new system OR
       a new component that we want to use in old system.
    -> So this can rarely communicate without requiring any code changes.
    -> But, changing the code is not always possible. May be because of following reasons:
        1. No access of old system
        2. Maybe its impractical
Solution:
    -> We can write extra layer that makes all the required modifications for enabling the communication between
       the two interfaces.
    -> This layer is called Adapter design pattern

Realtime application uses Adapter design patterns:
    1. Pyramid web framework
    2. Zope related frameworks
    3. Plone CMS

"""


class Club:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Club: {self.name}"

    def organize_event(self) -> None:
        print(f"{self.name}: Hires artist to perform for peoples")


class Musician:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Musician: {self.name}"

    def play(self) -> None:
        print(f"{self.name}: plays music")


class Dancer:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Dancer: {self.name}"

    def dance(self) -> None:
        print(f"{self.name}: Performs dance")


class Adapter:
    def __init__(self, obj, adapted_methods: dict) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self) -> str:
        return str(self.obj)


def main():
    objects = [Club("Nice Club"), Musician("Joy"), Dancer("Michale")]
    for obj in objects:
        if hasattr(obj, "play") or hasattr(obj, "dance"):
            if hasattr(obj, "play"):
                adapted_methods = dict(organize_event=obj.play)
            elif hasattr(obj, "dance"):
                adapted_methods = dict(organize_event=obj.dance)

            obj = Adapter(obj, adapted_methods)
        obj.organize_event()


if __name__ == '__main__':
    main()
