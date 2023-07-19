from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    valid_computer_types = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if not ComputerStoreApp.valid_computer_types.get(type_computer):
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = ComputerStoreApp.valid_computer_types[type_computer](manufacturer, model)
        self.warehouse.append(computer)
        return computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                computer_for_sale = computer
                break
        else:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer_for_sale.price
        self.warehouse.remove(computer_for_sale)

        return f"{computer_for_sale} sold for {client_budget}$."
