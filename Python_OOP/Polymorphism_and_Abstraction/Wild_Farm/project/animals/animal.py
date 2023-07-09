from abc import ABC, abstractmethod
from typing import List, Optional

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten
        
    @property
    @abstractmethod
    def suitable_food(self) -> List[Food]:
        pass

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass

    @abstractmethod
    def feed(self, food: Food) -> Optional[str]:
        pass


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    @property
    @abstractmethod
    def suitable_food(self):
        pass

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    @property
    @abstractmethod
    def suitable_food(self):
        pass

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

