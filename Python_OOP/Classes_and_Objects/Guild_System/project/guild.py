from typing import List

from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.guild_default:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        player.guild = Player.guild_default
        self.players.remove(player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        players = "\n".join([player.player_info() for player in self.players])

        return f"Guild: {self.name}\n{players}"
