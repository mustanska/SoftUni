from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    @property
    def sponsors(self):
        sponsors_dict = {"Petronas": {1: 1000000, 3: 500000}, "TeamViewer": {5: 100000, 7: 50000}}
        return sponsors_dict

    @property
    def expenses(self):
        return 200000
