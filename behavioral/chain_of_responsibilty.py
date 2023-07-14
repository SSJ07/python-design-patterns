"""
Chain of responsibility design pattern
-> It's equivalent of if....elif....elif...else condition.
"""
from abc import ABC, abstractmethod
from typing import Optional, Any

from creational.abstract_factory.game_factory import FrogWorld, GameEnvironment, WizardWorld, ArmyWorld


class GameHandler(ABC):

    def __init__(self, successor: Optional["GameHandler"] = None) -> None:
        self.successor = successor

    def start_game(self, age: int) -> None:
        resp = self.check_age(age)
        if not resp and self.successor:
            self.successor.start_game(age)
        elif resp:
            print(f"Starting game: {resp}")
            GameEnvironment(resp).play()
            print(f"Finished game: {resp}")

    @abstractmethod
    def check_age(self, age: int) -> Optional[bool]:
        pass


class FrogGameHandler(GameHandler):
    def check_age(self, age: int) -> Optional[Any]:
        if 1 <= age < 18:
            return FrogWorld("Frog")
        return None


class WizardGameHandler(GameHandler):
    def check_age(self, age: int) -> Optional[bool]:
        if 18 <= age < 30:
            return WizardWorld("Wizard")
        return None


class ArmyGameHandler(GameHandler):
    def check_age(self, age: int) -> Optional[bool]:
        if 30 <= age < 50:
            return ArmyWorld("Army")
        return None


class FallbackHandler(GameHandler):

    def check_age(self, age: int) -> Optional[bool]:
        print(f"No any game handler available for age: {age}")
        return None


def main():

    frog = FrogGameHandler()
    wizard = WizardGameHandler()
    army = ArmyGameHandler(FallbackHandler())

    frog.successor = wizard
    wizard.successor = army

    for age in [17, 24, 45, 60]:
        frog.start_game(age)


if __name__ == '__main__':
    main()
