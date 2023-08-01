from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIAN[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def find_musician_by_name(self, name):
        try:
            musician = next(filter(lambda m: m.name == name, self.musicians))
        except StopIteration:
            raise Exception(f"{name} isn't a musician!")

        return musician

    def find_band_by_name(self, name):
        try:
            band = next(filter(lambda b: b.name == name, self.bands))
        except StopIteration:
            raise Exception(f"{name} isn't a band!")

        return band

    @staticmethod
    def find_member_in_band_by_name(name, band):
        try:
            member = next(filter(lambda m: m.name == name, band.members))
        except StopIteration:
            raise Exception(f"{name} isn't a member of {band.name}!")

        return member


    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_musician_by_name(musician_name)
        band = self.find_band_by_name(band_name)
        band.add_member(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_band_by_name(band_name)
        member = self.find_member_in_band_by_name(musician_name, band)
        band.remove_member(member)
        return f"{musician_name} was removed from {band_name}."

    @staticmethod
    def is_band_has_enough_members(band_members):
        required_members = {"Guitarist": False, "Drummer": False, "Singer": False}

        for member_type in required_members:
            if any(filter(lambda m: m.__class__.__name__ == member_type, band_members)):
                required_members[member_type] = True

        return all(required_members.values())
    @staticmethod
    def is_band_ready_to_concert(concert_genre, band_members):
        genres = {
            "Rock": {
                "Drummer": ["play the drums with drumsticks"],
                "Singer": ["sing high pitch notes"],
                "Guitarist": ["play rock"]
            },
            "Metal": {
                "Drummer": ["play the drums with drumsticks"],
                "Singer": ["sing low pitch notes"],
                "Guitarist": ["play metal"]
            },
            "Jazz": {
                "Drummer": ["play the drums with drum brushes"],
                "Singer": ["sing high pitch notes", "sing low pitch notes"],
                "Guitarist": ["play jazz"]
            }
        }

        genre_skills = genres[concert_genre]

        for member in band_members:
            for skill in genre_skills[member.__class__.__name__]:
                if skill not in member.skills:
                    return False

        return True

    def start_concert(self, concert_place: str, band_name: str):
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        band = next(filter(lambda b: b.name == band_name, self.bands))

        if not self.is_band_has_enough_members(band.members):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if not self.is_band_ready_to_concert(concert.genre, band.members):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
