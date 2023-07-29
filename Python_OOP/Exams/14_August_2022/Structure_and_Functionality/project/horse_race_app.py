from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []
        self.created_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in HorseRaceApp.VALID_HORSES_TYPES:
            horse = HorseRaceApp.VALID_HORSES_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in self.created_races:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        self.created_races.append(race_type)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = [h for h in self.horses if h.__class__.__name__ == horse_type][-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if not horse.is_taken:
            if jockey.horse:
                return f"Jockey {jockey_name} already has a horse."

            jockey.horse = horse
            horse.is_taken = True
            return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def find_horse_race(self, race_type):
        try:
            horse_race = [hr for hr in self.horse_races if hr.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        return horse_race

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.find_horse_race(race_type)

        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.find_horse_race(race_type)

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        for jockey in horse_race.jockeys:
            if not winner:
                winner = jockey
            else:
                if winner.horse.speed < jockey.horse.speed:
                    winner = jockey

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."

