from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget
    
    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self) -> Dict[str, Dict[int, int]]:
        pass

    @property
    @abstractmethod
    def expenses(self) -> int:
        pass

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0

        for sponsor in self.sponsors.values():
            for pos, value in sponsor.items():
                if pos >= race_pos:
                    revenue += value
                    break

        revenue -= self.expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
