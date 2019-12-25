from collections import defaultdict

import JsonReader
from RiotAPI import RiotAPI


def main():
    key = ""
    with open("key.txt", "r") as key_file:
        key = key + key_file.readline()
    api = RiotAPI(key)

    summoner_puuid = api.get_summoner_by_name("puporr4uga")["puuid"]
    # last_20_matches = api.get_tft_match_by_player_puuid(summoner_puuid, 20)

    response = api.get_tft_match_by_match_id("BR1_1821009083")
    JsonReader.write_json(response, "a.json")

    cost_champions = defaultdict(lambda: set())
    trait_champions = defaultdict(lambda: set())
    all_champions = JsonReader.read_tft_champions_static_data()
    all_traits = JsonReader.read_tft_traits_static_data()

    for trait in all_traits:
        trait_champions[trait["name"]] = set()

    for champ in all_champions:
        cost_champions[champ["cost"]].add(champ["champion"])
        for trait in champ["traits"]:
            trait_champions[trait].add(champ["champion"])

    print(trait_champions)
    print(cost_champions)


#def get_my_team():


if __name__ == "__main__":
    main()
