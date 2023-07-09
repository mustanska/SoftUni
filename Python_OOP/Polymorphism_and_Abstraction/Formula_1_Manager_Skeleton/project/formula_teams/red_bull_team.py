from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    @property
    def sponsors(self):
        sponsors_dict = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}
        return sponsors_dict

    @property
    def expenses(self):
        return 250000
