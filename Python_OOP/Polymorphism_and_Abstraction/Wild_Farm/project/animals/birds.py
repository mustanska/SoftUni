from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Seed, Fruit


class Owl(Bird):
    @property
    def suitable_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Food):
        food_name = food.__class__.__name__
        if food.__class__ not in self.suitable_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    @property
    def suitable_food(self):
        return [Vegetable, Meat, Seed, Fruit]

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):
        if food.__class__ not in self.suitable_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity


