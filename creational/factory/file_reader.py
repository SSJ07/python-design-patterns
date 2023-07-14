"""
Factory method design pattern can be used to read different types of files.
e.g: Json file, XML file, text file.
"""
import json
import tempfile
from abc import ABC, abstractmethod
from xml.etree import ElementTree


class FileReader(ABC):

    @abstractmethod
    def read_data(self, file_path: str):
        pass


class JsonFileReader(FileReader):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_data(self) -> None:
        """
        >>>with open(self.file_path, "r") as fl:
        >>>    data = json.dumps(fl.read())
        """
        print(f"Reading json data from {self.file_path} file")


class XMLFileReader(FileReader):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_data(self) -> None:
        """
        >>> element_tree = ElementTree.parse(self.file_path)
        >>> element_tree.getroot()
        """
        print(f"Reading xml file content with ElementTree from file: {self.file_path}")


class TextFileReader(FileReader):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_data(self) -> None:
        """
        >>>with open(self.file_path, "r") as fl:
        >>>fl.read()
        """
        print(f"Reading text file content from : {self.file_path} file")


class FileReaderFactory:

    @staticmethod
    def create_file_reader(file_path: str) -> FileReader:
        if file_path.endswith(".json"):
            return JsonFileReader(file_path)
        elif file_path.endswith(".xml"):
            return XMLFileReader(file_path)
        elif file_path.endswith(".txt"):
            return TextFileReader(file_path)
        else:
            print(f"File {file_path} is not supported!")


def main():
    json_reader = FileReaderFactory.create_file_reader("skills.json")
    json_reader.read_data()

    xml_reader = FileReaderFactory.create_file_reader("skills.xml")
    xml_reader.read_data()

    text_reader = FileReaderFactory.create_file_reader("skills.txt")
    text_reader.read_data()


if __name__ == '__main__':
    main()
