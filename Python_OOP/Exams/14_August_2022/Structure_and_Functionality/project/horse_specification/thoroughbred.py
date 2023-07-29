from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    @property
    def max_speed(self):
        return 140

    def train(self):
        self.speed = min(self.speed + 3, self.max_speed)
