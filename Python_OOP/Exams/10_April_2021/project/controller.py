from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    valid_aquariums = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    valid_decorations = {"Ornament": Ornament, "Plant": Plant}
    valid_fishes = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums: list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str) -> str:
        if aquarium_type not in Controller.valid_aquariums:
            return "Invalid aquarium type."

        aquarium = Controller.valid_aquariums[aquarium_type](aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str) -> str:
        if decoration_type not in Controller.valid_decorations:
            return "Invalid decoration type."

        decoration = Controller.valid_decorations[decoration_type]()

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str) -> str:
        try:
            decoration = [d for d in self.decorations_repository.decorations
                          if self.decorations_repository.find_by_type(decoration_type) != "None"][0]
        except IndexError:
            return f"There isn't a decoration of type {decoration_type}."

        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.add_decoration(decoration)
                self.decorations_repository.decorations.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float) -> str:
        if fish_type not in Controller.valid_fishes:
            return f"There isn't a fish of type {fish_type}."

        fish = Controller.valid_fishes[fish_type](fish_name, fish_species, price)

        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str) -> str:
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                fed_fish = aquarium.feed()
                return f"Fish fed: {fed_fish}"

    def calculate_value(self, aquarium_name: str) -> str:
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                fishes_price = sum([f.price for f in aquarium.fish])
                decorations_price = sum([d.price for d in aquarium.decorations])

                return f"The value of Aquarium {aquarium_name} is {fishes_price + decorations_price:.2f}."

    def report(self):
        result = ""

        for aquarium in self.aquariums:
            result += f"{aquarium}\n"

        return result

