import RiotConsts

class Unit:

    def __init__(self, character_name, tier, active=False, items_id=[]):
        self.active = active
        self.character_id = "TFT2_" + character_name.title()
        self.name = character_name.title()
        self.items = items_id
        self.rarity = -1
        for cost, champs in RiotConsts.COST_CHAMPIONS.items():
            if self.name in champs:
                self.rarity = cost - 1
        self.tier = tier

    def level_up(self):
        self.tier = self.tier + 1

    def play_unit(self):
        self.active = True

    def remove_unit(self):
        self.active = False

    def get_unit_traits(self):
        traits = []
        for trait, champions in RiotConsts.TRAIT_CHAMPIONS.items():
            if self.name.casefold() in champions:
                traits.append(trait)
        return traits

    def __str__(self):
        return "Name: {}\nTier: {}\n".format(self.name, self.tier)
