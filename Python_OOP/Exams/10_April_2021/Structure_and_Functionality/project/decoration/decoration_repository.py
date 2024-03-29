from typing import Union

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations: list = []

    def add(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration) -> bool:
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str) -> Union[BaseDecoration, str]:
        try:
            decoration = [d for d in self.decorations if d.__class__.__name__ == decoration_type][0]
        except IndexError:
            return "None"

        return decoration

