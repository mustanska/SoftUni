from typing import Optional


class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> Optional[str]:
        if self.capacity >= people and not self.is_taken:
            self.is_taken = True
            self.guests = people
        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self) -> Optional[str]:
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
        else:
            return f"Room number {self.number} is not taken"

