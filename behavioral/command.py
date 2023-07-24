"""
Command design pattern

--> Its behavioral design pattern
--> It used to implement loose coupling in a request-response model
--> Basically, It decouples object that invokes command from an object who knows how to do that

Example:
    We can assume commands that handles different file operations like: create, read, delete files.
"""
import logging
import os.path
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FileOperation(ABC):

    @abstractmethod
    def execute(self):
        pass


class ReadFile(FileOperation):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def execute(self) -> None:
        if not os.path.isfile(self.file_path):
            logger.error(f"File: {self.file_path} does not exist")
            raise Exception(f"File: {self.file_path} does not exist")

        with open(self.file_path, "r") as fl:
            content = fl.read()
            logger.info(f"File contents are : {content}")

    def undo(self) -> None:
        if not os.path.isfile(self.file_path):
            logger.error(f"File: {self.file_path} does not exist")
            return None
        logger.info(f"Reverting file creation by removing file: {self.file_path}")
        os.remove(self.file_path)
        logger.info(f"Removed file: {self.file_path}")


class RenameFile(FileOperation):

    def __init__(self, src: str, dest: str) -> None:
        self.src = src
        self.dest = dest

    def execute(self) -> None:
        if not os.path.isfile(self.src) or not self.dest:
            logger.error("Source and destination file name must be provided.")
            raise Exception("Source or dest file name is missing. Must be provided both")

        os.rename(self.src, self.dest)
        logger.info(f"File {self.src} is renamed to {self.dest}")

    def undo_rename(self) -> None:
        logger.info("Performing undo operation for renamed file.")
        os.rename(self.dest, self.src)
        logger.info("Reverted rename file operation.")


class DeleteFile(FileOperation):

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def execute(self) -> None:
        if not os.path.isfile(self.file_path):
            logger.error(f"File {self.file_path} does not exist")
            raise Exception(f"File {self.file_path} does not exist")

        os.remove(self.file_path)
        logger.info(f"File {self.file_path} removed successfully")


class CreateFile(FileOperation):

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def execute(self) -> None:
        if os.path.isfile(self.file_path):
            logger.warning(f"File {self.file_path} is already exist. Skipped file operation")
            return None

        with open(self.file_path, "w") as fl:
            text = input("Enter some text: ")
            fl.write(text)

        logger.info(f"File {self.file_path} is created")


class FileCommands:

    def __init__(self) -> None:
        self.commands = {
            "1": CreateFile,
            "2": ReadFile,
            "3": RenameFile,
            "4": DeleteFile
        }

    def execute(self) -> None:
        logger.info("\nAvailable file commands are:\n1. CreateFile\n2.ReadFile\n3.RenameFile\n4.DeleteFile\n5.Quite \n")
        choice = input("Enter your choice: ")
        file_name = "demo.txt"
        while choice:
            if choice == "1":
                create_file = self.commands.get(choice)
                create_file(file_name).execute()
            elif choice == "2":
                read_file = self.commands.get(choice)
                read_file(file_name).execute()
            elif choice == "3":
                rename_file = self.commands.get(choice)(src=file_name, dest="demo1.txt")
                rename_file.execute()
                rename_file.undo_rename()
            elif choice == "4":
                delete_file = self.commands.get(choice)
                delete_file(file_name).execute()
            elif choice == "5":
                logger.info("Exiting from commands ops.")
                return None

            choice = input("Enter your choice: ")


if __name__ == '__main__':
    file_commands = FileCommands()
    file_commands.execute()
