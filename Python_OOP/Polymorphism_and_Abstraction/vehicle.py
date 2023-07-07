from abc import ABC, abstractmethod


class Vehicle(ABC):
    fuel_for_air_conditioner = 1

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass


class Car(Vehicle):
    fuel_for_air_conditioner = 0.9

    def drive(self, distance: int) -> None:
        fuel_needed = (self.fuel_consumption + self.fuel_for_air_conditioner) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    fuel_for_air_conditioner = 1.6

    def drive(self, distance: int) -> None:
        fuel_needed = (self.fuel_consumption + self.fuel_for_air_conditioner) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
