from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        ...


class Cat(Animal):
    def make_sound(self):
        return f"The sound of {self.name} is meow."


class Dog(Animal):
    def make_sound(self):
        return f"The sound of {self.name} is woof-woof."


class Chicken(Animal):
    def make_sound(self):
        return f"The sound of {self.name} is cluck."


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat("Cat"), Dog("Dog"), Chicken("Chicken")]
animal_sound(animals)

