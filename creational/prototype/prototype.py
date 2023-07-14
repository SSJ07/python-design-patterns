"""
Prototype design pattern

1. Used to create object from existing object.
2. It's basically clones the object
"""
import copy
import datetime


class Website:

    def __init__(self, domain: str, name: str, author: str, **kwargs) -> None:
        self.author = author
        self.name = name
        self.domain = domain

        for key, val in kwargs.items():
            setattr(self, key, val)

    def __str__(self) -> str:
        dis = vars(self).items()
        summary = []
        for k, v in sorted(dis):
            summary.append(f"{k}: {v}, ")
        return "".join(summary)


class Prototype:

    def __init__(self) -> None:
        self.objects = {}

    def register(self, identifier: str, website: Website) -> None:
        self.objects[identifier] = website

    def deregister(self, identifier: str) -> None:
        del self.objects[identifier]

    def clone(self, identifier: str, **attrs) -> object:
        _obj = self.objects.get(identifier)
        if not _obj:
            raise ValueError(f"Object not found for {identifier}")

        new_obj = copy.deepcopy(_obj)
        for key in attrs:
            setattr(new_obj, key, attrs[key])

        return new_obj


def main():
    website_1 = Website(domain="www.demo.com", name="Demo", author="Shri")

    prototype = Prototype()
    prototype.register("demo", website_1)

    new_website = prototype.clone("demo", domain="www.demo1.com", name="Demo1", created_date=datetime.datetime.now())

    print(f"original website: {website_1}")
    print(f"Cloned website: {new_website}")

    print(f"ID of website_1 : {id(website_1)} == {id(new_website)} ID of new_website")


if __name__ == '__main__':
    main()
