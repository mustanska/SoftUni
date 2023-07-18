import operator

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    valid_astronauts = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository: PlanetRepository = PlanetRepository()
        self.astronaut_repository: AstronautRepository = AstronautRepository()
        self.missions_completed = 0
        self.missions_missed = 0

    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        if not SpaceStation.valid_astronauts.get(astronaut_type):
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = SpaceStation.valid_astronauts[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str) -> str:
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str) -> str:
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self) -> None:
        [a.increase_oxygen(10) for a in self.astronaut_repository.astronauts]

    def sort_astronaut_by_highest_oxygen(self):
        return sorted(self.astronaut_repository.astronauts, key=operator.attrgetter('oxygen'), reverse=True)

    def send_on_mission(self, planet_name: str) -> str:
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        astronauts_for_mission = []

        for astronaut in self.sort_astronaut_by_highest_oxygen():
            if len(astronauts_for_mission) >= 5:
                break

            if astronaut.oxygen > 30:
                astronauts_for_mission.append(astronaut)

        if not astronauts_for_mission:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_count = 0
        for astronaut in astronauts_for_mission:
            astronauts_count += 1
            while astronaut.oxygen > 0:
                try:
                    astronaut.backpack.append(planet.items.pop())
                    astronaut.breathe()
                except IndexError:
                    self.missions_completed += 1
                    return f"Planet: {planet_name} was explored. {astronauts_count} astronauts " \
                           f"participated in collecting items."

        self.missions_missed += 1
        return "Mission is not completed."

    def report(self) -> str:
        astronauts = "\n".join([str(a) for a in self.astronaut_repository.astronauts])
        return f"{self.missions_completed} successful missions!\n" \
               f"{self.missions_missed} missions were not completed!\n" \
               f"Astronauts' info:\n{astronauts}"
