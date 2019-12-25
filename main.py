import JsonReader
from RiotAPI import RiotAPI


def main():
    key = ""
    with open("key.txt", "r") as key_file:
        key = key + key_file.readline()
    api = RiotAPI(key)
    print(key)

    summoner_puuid = api.get_summoner_by_name("moreninha52")["puuid"]
    last_20_matches = api.get_tft_match_by_player_puuid(summoner_puuid, 20)
    print(last_20_matches)

    response = api.get_tft_match_by_match_id("BR1_1821009083")
    print(response)

    print(response["metadata"])
    print(response["info"])

    print(JsonReader.read_tft_champions_static_data())


if __name__ == "__main__":
    main()
