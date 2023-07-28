from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        ...

    @abstractmethod
    def create_sofa(self):
        ...

    @abstractmethod
    def create_table(self):
        ...

class Chair:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sofa:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Table:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class VictorianFactory(AbstractFactory):
    def create_table(self):
        return Table("Victorian table")

    def create_sofa(self):
        return Sofa("Victorian sofa")

    def create_chair(self):
        return Chair("Victorian chair")


class ModernFactory(AbstractFactory):
    def create_table(self):
        return Table("Modern table")

    def create_sofa(self):
        return Sofa("Modern sofa")

    def create_chair(self):
        return Chair("Modern chair")

class FuturisticFactory(AbstractFactory):
    def create_table(self):
        return Table("Futuristic table")

    def create_sofa(self):
        return Sofa("Futuristic sofa")

    def create_chair(self):
        return Chair("Futuristic chair")

