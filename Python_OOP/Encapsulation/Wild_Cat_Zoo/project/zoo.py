from typing import List

from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        is_animals_capacity_left = len(self.animals) < self.__animal_capacity
        is_budget = self.__budget >= price

        if is_budget and is_animals_capacity_left:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if is_animals_capacity_left and not is_budget:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salaries = sum([w.salary for w in self.workers])

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        moneys_for_care = sum([a.money_for_care for a in self.animals])

        if self.__budget >= moneys_for_care:
            self.__budget -= moneys_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join([f"{l}" for l in lions])
        result += f"\n----- {len(tigers)} Tigers:\n"
        result += "\n".join([f"{t}" for t in tigers])
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join([f"{c}" for c in cheetahs])

        return result

    def workers_status(self) -> str:
        keepers = [k for k in self.workers if isinstance(k, Keeper)]
        caretakers = [c for c in self.workers if isinstance(c, Caretaker)]
        vets = [v for v in self.workers if isinstance(v, Vet)]

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([f"{k}" for k in keepers])
        result += f"\n----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([f"{c}" for c in caretakers])
        result += f"\n----- {len(vets)} Vets:\n"
        result += "\n".join([f"{v}" for v in vets])

        return result

