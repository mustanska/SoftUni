
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        people = 2
        super().__init__(family_name, pension_one + pension_two, people)
        self.room_cost = 15
        self.appliances: list = [TV(), Fridge(), Stove()] * people
        self.calculate_expenses(self.appliances)
