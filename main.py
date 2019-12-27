from collections import defaultdict

import JsonReader
import RiotConsts
from RiotAPI import RiotAPI
from Team import Team
from Unit import Unit


def main():
    api = get_api_object()

    summoner_puuid = api.get_summoner_by_name("moreninha52")["puuid"]
    last_20_matches = api.get_tft_match_by_player_puuid(summoner_puuid, 20)

    response = api.get_tft_match_by_match_id("BR1_1821009083")
    # print(response)
    JsonReader.write_json(response, "a.json")

    # print(RiotConsts.TRAIT_CHAMPIONS)
    # print(RiotConsts.COST_CHAMPIONS)

    owned_units_and_tiers = get_my_team()

    my_active_units = []
    my_stored_units = []
    for champ, tier in owned_units_and_tiers[0].items():
        my_active_units.append(Unit(champ, tier, True))
    for champ, tier in owned_units_and_tiers[1].items():
        my_stored_units.append(Unit(champ, tier, False))

    # print(my_units[3].getUnitTraits())

    my_team = Team(my_active_units, my_stored_units)

    print(my_team.get_active_team_traits())
    print(my_team.get_inactive_team_traits())
    print(RiotConsts.TRAIT_SETS)


def get_api_object():
    key = ""
    with open("key.txt", "r") as key_file:
        key = key + key_file.readline()
    api = RiotAPI(key)
    return api


def get_my_team():
    my_active_team = defaultdict(list)
    my_stored_team = defaultdict(list)
    print("Active Champions in game:")
    inp = input("Champion tier: ")
    while len(inp) > 2:
        champ, tier = inp.split()
        my_active_team[champ].append(int(tier))
        inp = input("Champion tier: ")
    print("Stored Champions in game:")
    inp = input("Champion tier: ")
    while len(inp) > 2:
        champ, tier = inp.split()
        my_stored_team[champ].append(int(tier))
        inp = input("Champion tier: ")

    return my_active_team, my_stored_team


if __name__ == "__main__":
    main()
