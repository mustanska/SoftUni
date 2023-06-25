from typing import Dict


class Player:
    guild_default = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str, int] = {}
        self.guild: str = Player.guild_default

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if (skill_name, mana_cost) in self.skills.items():
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        skills = "\n".join([f"==={name} - {mana_cost}" for name, mana_cost in self.skills.items()])

        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skills}"

