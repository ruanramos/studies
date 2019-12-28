from collections import defaultdict
import RiotConsts
from itertools import permutations, combinations


class Team:

    def __init__(self, active_units, stored_units, level):
        self.active_units = active_units
        self.stored_units = stored_units
        self.all_units = active_units + stored_units
        self.level = level

    def get_active_team_traits(self):
        traits = defaultdict(lambda: 0)
        counted_units = set()
        for unit in self.active_units:
            if unit.active and unit.name not in counted_units:
                for trait in unit.get_unit_traits():
                    traits[trait] = traits[trait] + 1

        return traits

    def get_inactive_team_traits(self):
        traits = defaultdict(lambda: 0)
        counted_units = set()
        for unit in self.stored_units:
            if not unit.active and unit.name not in counted_units:
                counted_units.add(unit.name)
                for trait in unit.get_unit_traits():
                    traits[trait] = traits[trait] + 1
        return traits


    def calculate_possible_teams(self):
        # TODO Correct this method
        possible_traits = {}
        combs = list(combinations(self.all_units, self.level))
        for possible_team in combs:
            l = list(possible_team)
            team = Team(l, [], len(l))
            s = ""
            for u in team.all_units:
                s = s + str(u)
            possible_traits[s] = team.get_active_team_traits()
        return possible_traits