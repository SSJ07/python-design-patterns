"""
Proxy design pattern

--> Proxy design pattern is another structural design pattern
--> It allows you to provide substitute or placeholder for original object
--> A proxy controls access of original object and allows something to perform before or after accessing original object
--> It used to performs important actions before accessing original object
--> Below are few well-know proxy types:
    1. A remote proxy: Act as local representation of an object that really exist in different location
    2. A virtual proxy: It uses lazy initialization of an object until it's really not required
    3. A protection/protective proxy: Which controls access to a sensitive object
    4. A smart(reference) proxy: Which performs extra activity when an object is accessed

Example:
    ORM(Object relational mapping) is a very good example of proxy. It acts as proxy and access control of database
    which could be local or remote.
"""


from typing import List


class SensitiveInfo:

    def __init__(self) -> None:
        self.users: List[str] = []

    def read(self) -> None:
        print(f"List of all users are : {self.users}")

    def add(self, user) -> None:
        print(f"Adding user : {user}")
        self.users.append(user)


class Info:
    """Protected proxy to SensitiveInfo"""

    def __init__(self) -> None:
        self.sensitive_info = SensitiveInfo()
        self.secret = "ABcDE12"  # Just for demo purpose, Not recommended hardcoded secret or passwords in source code

    def read(self) -> None:
        self.sensitive_info.read()

    def add(self, user) -> None:
        sec = input("Enter secret code: ")
        if sec == self.secret:
            self.sensitive_info.add(user)


def main():
    """Client code"""
    info = Info()

    while True:
        print("\n 1. Read users \n 2. Add user \n 3. quite \n")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            info.read()
        elif choice == '2':
            user = input("\nEnter username to add: ")
            info.add(user)
        elif choice == '3':
            exit()
        else:
            print("Invalid choice")
            exit()


if __name__ == '__main__':
    main()
