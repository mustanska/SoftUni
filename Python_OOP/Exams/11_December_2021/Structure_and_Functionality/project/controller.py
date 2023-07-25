import operator
from typing import List

from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    valid_cars = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: list = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int) -> str:
        if Controller.valid_cars.get(car_type):
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")

            car = Controller.valid_cars[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str:
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str:
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str:
        try:
            driver = [d for d in self.drivers if d.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")

        try:
            cars = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
            car = cars[-1]
        except IndexError:
            raise Exception(f"Car {car_type} could not be found!")

        if not driver.car:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

        old_car = driver.car
        driver.car.is_taken = False
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str) -> str:
        try:
            race = [r for r in self.races if r.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = [d for d in self.drivers if d.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str) -> str:
        try:
            race = [r for r in self.races if r.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = []

        for idx, driver in enumerate(sorted(race.drivers, key=operator.attrgetter("car.speed_limit"), reverse=True)):
            if idx > 2:
                break

            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(result)
