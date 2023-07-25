"""
Observer design pattern

--> Observer design pattern is behavior design pattern
--> It used when a group of objects needs to be changed when the state of another object get changed.
--> The Observer design pattern describes a publish-subscriber model
    --> Publisher = Subject/Observable <-- Single Object (Model - 1)
    --> Subscriber = Observers <-- one or more objects (Views - 2)

Example:
    --> Model-view-controller(MVC) is good example of observer design pattern
    --> Assume we are using the data of same model in two different views.
        Whenever the model is modified, both views needs to be updated.
"""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Publisher:
    """Publisher that updates all observers"""

    def __init__(self) -> None:
        self.observers = []

    def add(self, observer: object) -> None:
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            logger.info(f"Observer {observer} is already exist")

    def remove(self, observer: object) -> None:
        try:
            self.observers.remove(observer)
        except ValueError:
            logger.error(f"Observer {observer} does not exist")

    def notify(self) -> None:
        [obs.notify(self) for obs in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int) -> None:
        try:
            self._data = int(value)
        except TypeError:
            logger.error("Invalid type")
        else:
            self.notify()

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self.name} has data {self._data}"


class HexFormatterObs:
    def notify(self, publisher) -> None:
        value = hex(publisher.data)
        logger.info(f"{type(self).__name__}: {publisher.name} has data {value}")


class BinaryFormatterObs:
    def notify(self, publisher) -> None:
        value = bin(publisher.data)
        logger.info(f"{type(self).__name__}: {publisher.name} has data {value}")


def main():
    """Entrypoint of app"""
    df = DefaultFormatter("DefaultFormatter")

    hf = HexFormatterObs()
    df.add(hf)
    df.data = 3

    bn = BinaryFormatterObs()
    df.add(bn)
    df.data = 5


if __name__ == '__main__':
    main()
