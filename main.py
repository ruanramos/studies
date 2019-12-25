import JsonReader
import RiotConsts
from RiotAPI import RiotAPI
from Unit import Unit


def main():
    key = ""
    with open("key.txt", "r") as key_file:
        key = key + key_file.readline()
    api = RiotAPI(key)

    summoner_puuid = api.get_summoner_by_name("puporr4uga")["puuid"]
    # last_20_matches = api.get_tft_match_by_player_puuid(summoner_puuid, 20)

    response = api.get_tft_match_by_match_id("BR1_1821009083")
    JsonReader.write_json(response, "a.json")

    print(RiotConsts.TRAIT_CHAMPIONS)
    print(RiotConsts.COST_CHAMPIONS)

    my_team = get_my_team()
    my_units = []
    print(my_team)
    for champ, tier in my_team.items():
        my_units.append(Unit(champ, tier))

    for u in my_units:
        print(u)

def get_my_team():
    my_team = {}
    inp = input("Champion tier: ")
    while len(inp) > 2:
        champ, tier = inp.split()
        my_team[champ] = tier
        inp = input("Champion tier: ")
    return my_team


if __name__ == "__main__":
    main()
