"""
The Facade design pattern

--> The Facade design pattern that provides simplified interface that handles complex internal system
--> The Facade design pattern act as abstraction layer for complex system
--> The most usual reason to use facade design pattern is for providing single and simple entry point to a complex
    system.
--> By introducing facade design pattern, the client code can use a system by simply calling single method/function.
    At same time , the internal system doesn't lose any functionality, it just encapsulates it.
--> Facade design pattern give extra benefit of client code not required to modify even we modify internal structure.


Problem:
    --> Suppose we have application with lots of classes and need do following things:
        1. Initialize all objects
        2. Keep track of all dependencies
        3. Execute all objects methods in correct order
        4. Make sure complex system works in right order

Example:
        Let's take example of Computer. A Computer is a complex machine with different parts.
        Each part are responsible to perform specific task and these should be in a right order.
        A Computer booting is complex procedure  like:
            1. CUP starts BIOS system from ROM
            2. BIOS performs hardware tests -> If fails --> Halt
            3. The bootloader must load into main memory from secondary(Hard)Disk
            4. CPU must boot operating system kernel
            5. Starts OS

        This is so complex for end user. So, instead of exposing all this procedure to client, We just encapsulate
        all this complexity in right order and provides simple interface like start button.
        When user just press start button all these complex system starts works in predefined order.

    Some other examples:
        1. Online Ordering system: Online ordering system provides simple interface to place an order and internally
            it perform different operations like packaging, transport, delivery,
        1. Starting car with pressing single button(facade). Car has different parts and complex system internally.
        2. Customer support department(facade) for end user:
            Company has customer support which act facade and responsible to deal with all other
            departments of Company like billing, technical support, general assistant and so on.
"""
from abc import ABC, abstractmethod
from enum import Enum


class State(Enum):
    new = "new"
    running = "running"
    sleeping = "sleeping"
    restart = "restart"
    zombie = "zombie"


class Server(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):

    def __init__(self) -> None:
        self.name = "FileServer"
        self.state = State.new

    def boot(self) -> None:
        print("Booting FileServer.....")
        self.state = State.running

    def kill(self, restart=True) -> None:
        print(f"Stopping {self.name}...")
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions) -> None:
        print(f"{self.name}: Creating file {name} for user: {user} with permissions: {permissions}")


class ProcessServer(Server):
    def __init__(self) -> None:
        self.name = "ProcessServer"
        self.state = State.new

    def boot(self) -> None:
        print(f"Booting {self.name}")
        self.state = State.running

    def kill(self, restart=True) -> None:
        print(f"Stopping {self.name}")
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name) -> None:
        print(f"{self.name}:: Creating process {name} for the user {user}")


class OperatingSystem:
    """The facade"""

    def __init__(self) -> None:
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self) -> None:
        for server in [self.fs, self.ps]:
            server.boot()

    def create_file(self, user, name, permissions) -> None:
        self.fs.create_file(user, name, permissions)

    def create_process(self, user, name) -> None:
        self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.fs.create_file("A", "File.txt", "rwx")
    os.ps.create_process("B", "Process1")


if __name__ == '__main__':
    main()
