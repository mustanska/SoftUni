from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    @property
    def suitable_food(self):
        return [Vegetable, Fruit]

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__ not in self.suitable_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 0.10
        self.food_eaten += food.quantity


class Dog(Mammal):
    @property
    def suitable_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__ not in self.suitable_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity


class Cat(Mammal):
    @property
    def suitable_food(self):
        return [Meat, Vegetable]

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Food):
        if food.__class__ not in self.suitable_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Tiger(Mammal):
    @property
    def suitable_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__ not in self.suitable_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 1
        self.food_eaten += food.quantity



