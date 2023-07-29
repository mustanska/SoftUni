from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    @property
    def max_speed(self):
        return 120

    def train(self):
        self.speed = min(self.speed + 2, self.max_speed)
