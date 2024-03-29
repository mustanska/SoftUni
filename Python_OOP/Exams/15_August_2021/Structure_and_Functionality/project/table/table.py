from abc import ABC, abstractmethod
from typing import Optional

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: list = []
        self.drink_orders: list = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    def reserve(self, number_of_people: int) -> None:
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood) -> None:
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink) -> None:
        self.drink_orders.append(drink)

    def get_bill(self) -> float:
        total_foods_price = sum([f.price for f in self.food_orders])
        total_drinks_price = sum([d.price for d in self.drink_orders])

        return total_foods_price + total_drinks_price

    def clear(self) -> None:
        self.drink_orders.clear()
        self.food_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self) -> Optional[str]:
        if not self.is_reserved:
            return f"Table: {self.table_number}\n"\
                   f"Type: {self.__class__.__name__}\n"\
                   f"Capacity: {self.capacity}"
