from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        people = 2
        super().__init__(family_name, salary_one + salary_two, people)
        self.room_cost = 20
        self.appliances: list = [TV(), Fridge(), Laptop()] * people
        self.calculate_expenses(self.appliances)
