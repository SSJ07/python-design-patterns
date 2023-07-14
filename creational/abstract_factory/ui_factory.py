from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self):
        pass


class CheckBox(ABC):

    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        print("Rendering windows button")


class WindowsCheckbox(CheckBox):
    def render(self):
        print("Rendering windows checkbox")


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsGUIFactory(GUIFactory):
    def create_checkbox(self):
        return WindowsCheckbox()

    def create_button(self):
        return WindowsButton()


class MacOSButton(Button):
    def render(self):
        print("Rendering MacOS button")


class MacOSCheckbox(CheckBox):
    def render(self):
        print("Rendering MacOS checkbox")


class MacOSGUIFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


def main():
    factories = [MacOSGUIFactory(), WindowsGUIFactory()]
    for factory in factories:
        button = factory.create_button()
        checkbox = factory.create_checkbox()

        button.render()
        checkbox.render()


if __name__ =='__main__':
    main()
