"""
@Author: Shrikant Jagtap

Singleton design pattern allows to create only one instance of class as central point of access.
Use case:
    1. Logger: We can create single logger instance and use throughout the application
"""


class SingletonDemo:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def main():
    """
    >>> first_instance = SingletonDemo()
    >>> second_instance = SingletonDemo()
    >>> third_instance = SingletonDemo()
    >>> (id(first_instance) == id(second_instance)) and (id(second_instance) == id(third_instance))
    True
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
