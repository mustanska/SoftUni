from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts: list = []

    def add(self, astronaut: Astronaut) -> None:
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut) -> None:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Astronaut:
        try:
            astronaut = [a for a in self.astronauts if a.name == name][0]
            return astronaut
        except IndexError:
            ...


