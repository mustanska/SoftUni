from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people) -> None:
        try:
            room = [r for r in self.rooms if r.number == room_number][0]

            if not room.is_taken and room.capacity >= people:
                room.take_room(people)
                self.guests += people

        except IndexError:
            pass

    def free_room(self, room_number) -> None:
        try:
            room = [r for r in self.rooms if r.number == room_number][0]

            if room.is_taken:
                self.guests -= room.guests
                room.free_room()
        except IndexError:
            pass

    def status(self) -> str:
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"

