from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)

        elif team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)

        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        red_bull_msg = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_msg = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        team_better_pos = "Mercedes" if mercedes_pos < red_bull_pos else "Red Bull"

        return f"Red Bull: {red_bull_msg}. Mercedes: {mercedes_msg}. {team_better_pos} is ahead at the {race_name} race."