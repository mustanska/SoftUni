from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        people = 1
        super().__init__(family_name, salary, people)
        self.room_cost = 10
        self.appliances: list = [TV()]
        self.calculate_expenses(self.appliances)

