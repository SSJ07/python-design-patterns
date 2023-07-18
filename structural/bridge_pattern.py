"""
Bridge design pattern

-> Adapter design pattern is used later to make unrelated classes work together
-> Bridge design pattern designed upfront to decouple implementation with its abstraction.

Example:
        InfoProduct (Up front implementation)
            ---> Info on marketplace
            ---> Website
            ---> Social_Media

Use Case:
    --> Bridge pattern is best design pattern to share implementation among multiple object.

Implementation:
    --> Building an application which going to manage and deliver content after fetching it from different sources
    --> Sources could be:
        --> A web page (Based on its URL)
        --> A resource accessed on an FTP server
        --> A file on local file system
        --> A database server
    --> Another implementation could be:
        1. Device drivers
        2. GUI
        3. Website builders
"""
import tempfile
import urllib.request
from abc import ABC, abstractmethod


class ResourceContent:
    """Maintainer class that reference to an object which represents the Implementor"""

    def __init__(self, rc_implementor) -> None:
        self.rc_implementor = rc_implementor

    def show_content(self, path: str) -> None:
        self.rc_implementor.fetch(path)


class ResourceContentFetcher(ABC):

    @abstractmethod
    def fetch(self, path: str) -> None:
        """Abstract method that needs to be implemented by different content fetcher classes"""


class URLFetcher(ResourceContentFetcher):

    def fetch(self, path: str) -> None:
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                content = response.read()
                print(f"Content Fetched from: {self.__class__.__name__} : {content}")


class LocalFileFetcher(ResourceContentFetcher):
    """Concrete implementation class for Implementor interface"""

    def fetch(self, path: str) -> None:
        with open(path) as fl:
            content = fl.read()
            print(f"Content Fetched from: {self.__class__.__name__}: {content}")


def main():
    """Entry point of application"""
    rc_fetcher = ResourceContent(URLFetcher())
    rc_fetcher.show_content(path="http://python.org")

    rc_fetcher = ResourceContent(LocalFileFetcher())
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"Local file server. Bridge design pattern")
    rc_fetcher.show_content(path=tmp.name)


if __name__ == '__main__':
    main()
