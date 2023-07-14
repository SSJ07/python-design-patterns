"""
@Author: Shrikant Jagtap

-> Abstract design pattern is generalization of factory design pattern.
-> Abstract factory is a logical group of factory methods, where each factory method is responsible for
generating different kind of object.

When to use abstract factory design pattern?
-> If we find out that our application requires many factory methods, which make sense to combine to create a family
    of objects, we end up with abstract factory.
"""
from abc import ABC, abstractmethod
from typing import Optional, Union


class Obstacle:

    def __init__(self, name: str, action: str) -> None:
        self.name = name
        self._action = action

    def __str__(self) -> str:
        return self.name

    def action(self) -> str:
        return self._action


class Game:

    def __init__(self, name: str) -> None:
        self.name = name

    def interact_with(self, obstacle: Obstacle):
        act = obstacle.action()
        print(f"{self.__class__.__name__} encountered obstacle: {obstacle} and act {act}")


class GameWorld(ABC):

    def __init__(self, name: str) -> None:
        self.player_name = name

    def __str__(self) -> str:
        return f"\n---------------------{self.__class__.__name__}--------------\n"

    @abstractmethod
    def make_character(self):
        pass

    @abstractmethod
    def make_obstacle(self):
        pass


class Frog(Game):
    pass


class Bug(Obstacle):
    pass


class FrogWorld(GameWorld):

    def make_character(self) -> Frog:
        return Frog(self.player_name)

    def make_obstacle(self) -> Bug:
        return Bug(name="a bug", action="eats it")


class WizardWorld(GameWorld):

    def make_character(self):
        class Wizard(Game):
            pass
        return Wizard(self.player_name)

    def make_obstacle(self):
        class Ork(Obstacle):
            pass
        return Ork(name="a Ork", action="Kills it")


class Army(Game):
    pass


class Shoots(Obstacle):
    pass


class ArmyWorld(GameWorld):
    def make_character(self):
        return Army(name="The army")

    def make_obstacle(self):
        return Shoots(name="a enemy", action="Shoots")


class GameEnvironment:

    def __init__(self, factory: Union[FrogWorld, WizardWorld, ArmyWorld]) -> None:
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self) -> None:
        self.hero.interact_with(self.obstacle)


def main():
    username = input("Hi, what is your name?")
    age = int(input(f"Hello: {username}, What's your age?"))

    game_type = FrogWorld if age <= 18 else WizardWorld

    print(f"--------------Hello {username}, Welcome to the {game_type.__class__} game. -------------\n")
    game = GameEnvironment(game_type(game_type.__name__))
    print(f"Starting to play {game_type.__name__} game.\n")
    game.play()
    print(f"Finished playing {game_type.__name__} game.\n")


if __name__ == '__main__':
    main()
