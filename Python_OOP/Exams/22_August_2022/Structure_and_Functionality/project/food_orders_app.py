from copy import copy

from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in FoodOrdersApp.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join([meal.details() for meal in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        shopping_cart = []
        bill = 0

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for meal_name, quantity in meal_names_and_quantities.items():
            try:
                meal = next(filter(lambda m: m.name == meal_name, self.menu))
            except StopIteration:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

            shopping_meal = copy(meal)
            shopping_meal.quantity = quantity
            shopping_cart.append(shopping_meal)
            bill += shopping_meal.price * quantity

        client.shopping_cart.extend(shopping_cart)
        client.bill += bill

        for client_meal in shopping_cart:
            menu_meal = next(filter(lambda m: m.name == client_meal.name, self.menu))
            menu_meal.quantity -= client_meal.quantity

        return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in client.shopping_cart])} for {client.bill:.2f}lv."


    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for client_meal in client.shopping_cart:
            meal = next(filter(lambda m: m.name == client_meal.name, self.menu))
            meal.quantity += client_meal.quantity

        client.shopping_cart.clear()
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.shopping_cart.clear()
        bill_paid = client.bill
        client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {bill_paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
