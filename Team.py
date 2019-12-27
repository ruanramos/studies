from collections import defaultdict


class Team:

    def __init__(self, active_units, stored_units):
        self.active_units = active_units
        self.stored_units = stored_units
        self.all_units = active_units + stored_units

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
