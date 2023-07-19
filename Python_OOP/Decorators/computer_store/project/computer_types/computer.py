from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str = None
        self.ram: int = None
        self.price: int = 0

    @property
    @abstractmethod
    def available_processors(self):
        ...
    
    @property
    @abstractmethod
    def max_ram_size(self):
        ...

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    def valid_ram_sizes(self):
        sizes = {}
        for number in range(2, self.max_ram_size + 1):
            if log2(number).is_integer():
                sizes[number] = int(log2(number))

        return sizes
    
    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    def configure_computer(self, processor: str, ram: int):
        if not self.available_processors.get(processor):
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if not self.valid_ram_sizes.get(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[processor] + self.valid_ram_sizes[ram] * 100

        return f"Created {self} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

