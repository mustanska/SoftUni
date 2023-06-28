class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int) -> None:
        fuel_needed = kilometers * self.fuel_consumption

        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
