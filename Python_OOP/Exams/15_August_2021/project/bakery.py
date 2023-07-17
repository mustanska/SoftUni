from typing import Tuple

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    valid_baked_food = {"Bread": Bread, "Cake": Cake}
    valid_drinks = {"Tea": Tea, "Water": Water}
    valid_tables = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: list = []
        self.drinks_menu: list = []
        self.tables_repository: list = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float) -> str:
        for food in self.food_menu:
            if food.name == name:
                raise ValueError(f"{food_type} {name} is already in the menu!")

        for key, value in Bakery.valid_baked_food.items():
            if key == food_type:
                food = value(name, price)
                self.food_menu.append(food)
                return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str) -> str:
        for drink in self.drinks_menu:
            if drink.name == name:
                raise ValueError(f"{drink_type} {name} is already in the menu!")

        for key, value in Bakery.valid_drinks.items():
            if key == drink_type:
                drink = value(name, portion, brand)
                self.drinks_menu.append(drink)
                return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> str:
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise ValueError(f"Table {table_number} is already in the bakery!")

        for key, value in Bakery.valid_tables.items():
            if key == table_type:
                table = value(table_number, capacity)
                self.tables_repository.append(table)
                return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        try:
            table = [t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people][0]

            table.number_of_people = number_of_people
            table.is_reserved = True
            return f"Table {table.table_number} has been reserved for {number_of_people} people"

        except IndexError:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: Tuple[str]) -> str:
        try:
            table = [t for t in self.tables_repository if t.table_number == table_number][0]

            food_names_missed: list = []

            for name in food_names:
                for food in self.food_menu:
                    if food.name == name:
                        table.order_food(food)
                        break
                else:
                    food_names_missed.append(name)

            ordered_food = "\n".join([str(f) for f in table.food_orders])
            missed_food = "\n".join(food_names_missed)

            result = f"Table {table_number} ordered:\n"\
                     f"{ordered_food}\n"\
                     f"{self.name} does not have in the menu:\n" \
                     f"{missed_food}"

            return result

        except IndexError:
            return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drinks_names: Tuple[str]) -> str:
        try:
            table = [t for t in self.tables_repository if t.table_number == table_number][0]

            drink_names_missed: list = []

            for name in drinks_names:
                for drink in self.drinks_menu:
                    if drink.name == name:
                        table.order_drink(drink)
                        break
                else:
                    drink_names_missed.append(name)

            ordered_drink = "\n".join([str(d) for d in table.drink_orders])
            missed_drink = "\n".join(drink_names_missed)

            result = f"Table {table_number} ordered:\n"\
                     f"{ordered_drink}\n"\
                     f"{self.name} does not have in the menu:\n" \
                     f"{missed_drink}"

            return result

        except IndexError:
            return f"Could not find table {table_number}"

    def leave_table(self, table_number: int) -> str:
        table = [t for t in self.tables_repository if t.table_number == table_number][0]
        bill = table.get_bill()
        self.total_income += bill
        table.clear()

        return f"Table: {table.table_number}\n"\
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self) -> str:
        result = []

        for table in self.tables_repository:
            if table.is_reserved:
                continue

            result.append(f"{table.free_table_info()}")

        return "\n".join(result)

    def get_total_income(self) -> str:
        return f"Total income: {self.total_income:.2f}lv"
