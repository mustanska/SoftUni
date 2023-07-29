from typing import List, Optional
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    valid_sustenance_types = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: list = []

    def add_player(self, *players) -> Optional[str]:
        added_names = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_names.append(player.name)

        return f"Successfully added: {', '.join(added_names)}"

    def add_supply(self, *supplies) -> None:
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str) -> str:
        try:
            player = [p for p in self.players if p.name == player_name][0]

        except IndexError:
            ...

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        if Controller.valid_sustenance_types.get(sustenance_type):
            try:
                idx, supply = [(i, s) for i, s in enumerate(self.supplies) if s.__class__.__name__ == sustenance_type][-1]
            except IndexError:
                supply_type = Controller.valid_sustenance_types[sustenance_type].type
                raise Exception(f"There are no {supply_type} supplies left!")

            player.stamina = min(player.stamina + supply.energy, 100)
            self.supplies.pop(idx)
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def check_stamina_players(*players) -> str:
        result = []

        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")

        return "\n".join(result)

    def duel(self, first_player_name: str, second_player_name: str) -> str:
        fp = next(filter(lambda p: p.name == first_player_name, self.players))
        sp = next(filter(lambda p: p.name == second_player_name, self.players))

        result = self.check_stamina_players(fp, sp)

        if result:
            return result

        attacker, attacked = (fp, sp) if fp.stamina < sp.stamina else (sp, fp)
        attacked.stamina = max(attacked.stamina - attacker.stamina / 2, 0)
        attacker.stamina = max(attacker.stamina - attacked.stamina / 2, 0)

        winner_name = attacker.name if attacker.stamina > attacked.stamina else attacked.name

        return f"Winner: {winner_name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __repr__(self):
        return "\n".join([str(p) for p in self.players]) + "\n" + "\n".join(s.details() for s in self.supplies)
