from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list = []
        self.fish: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self) -> int:
        total_comfort = sum([d.comfort for d in self.decorations])
        return total_comfort

    def add_fish(self, fish) -> str:
        if self.capacity <= len(self.fish):
            return "Not enough capacity."

        if fish.aquarium == self.__class__.__name__:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        else:
            return "Water not suitable."

    def remove_fish(self, fish) -> None:
        self.fish.remove(fish)

    def add_decoration(self, decoration) -> None:
        self.decorations.append(decoration)

    def feed(self) -> int:
        count = 0
        for fish in self.fish:
            value = fish.size
            fish.eat()
            if fish.size != value:
                count += 1

        return count

    def __str__(self):
        fishes = " ".join([f.name for f in self.fish]) if self.fish else "none"
        result = f"{self.name}:\nFish: {fishes}\n" \
                 f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"

        return result
