from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    def breathe(self) -> None:
        self.oxygen -= 10

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount

    def __repr__(self):
        backpack_items = ", ".join(self.backpack) if self.backpack else "none"
        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {backpack_items}"

