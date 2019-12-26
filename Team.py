from collections import defaultdict


class Team:

    def __init__(self, units):
        self.units = units

    def get_active_team_traits(self):
        traits = defaultdict(lambda: 0)
        counted_units = set()
        for unit in self.units:
            if unit.active and unit.name not in counted_units:
                for trait in unit.get_unit_traits():
                    traits[trait] = traits[trait] + 1
        return traits

    def get_inactive_team_traits(self):
        traits = defaultdict(lambda: 0)
        counted_units = set()
        for unit in self.units:
            if not unit.active and unit.name not in counted_units:
                counted_units.add(unit.name)
                for trait in unit.get_unit_traits():
                    traits[trait] = traits[trait] + 1
        return traits
