from collections import defaultdict

import JsonReader
from RiotAPI import RiotAPI
import RiotConsts
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

    u = Unit("zed", 3)
    print(u.name)
    print(u.items)
    print(u.character_id)
    print(u.tier)


#def get_my_team():


if __name__ == "__main__":
    main()
