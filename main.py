from collections import defaultdict

import JsonReader
import RiotConsts
from RiotAPI import RiotAPI
from Unit import Unit
from Team import Team


def main():
    key = ""
    with open("key.txt", "r") as key_file:
        key = key + key_file.readline()
    api = RiotAPI(key)

    summoner_puuid = api.get_summoner_by_name("moreninha52")["puuid"]
    last_20_matches = api.get_tft_match_by_player_puuid(summoner_puuid, 20)

    response = api.get_tft_match_by_match_id("BR1_1821009083")
    #print(response)
    JsonReader.write_json(response, "a.json")

    #print(RiotConsts.TRAIT_CHAMPIONS)
    #print(RiotConsts.COST_CHAMPIONS)

    owned_units_and_tiers = get_my_team()
    my_units = []
    for champ, tier in owned_units_and_tiers.items():
        my_units.append(Unit(champ, tier, True)) # adding units all as active

    #print(my_units[3].getUnitTraits())

    my_team = Team(my_units)
    print(my_team.get_active_team_traits())
    print(my_team.get_inactive_team_traits())
    print(RiotConsts.TRAIT_SETS)

def get_my_team():
    my_team = defaultdict(list)
    inp = input("Champion tier: ")
    while len(inp) > 2:
        champ, tier = inp.split()
        my_team[champ].append(int(tier))
        inp = input("Champion tier: ")
    return my_team


if __name__ == "__main__":
    main()
