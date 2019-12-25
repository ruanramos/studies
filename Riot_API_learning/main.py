from RiotAPI import RiotAPI
import JsonReader
import os


def main():
    api = RiotAPI(os.environ.get("RIOT_API_KEY"))
    # summoner_id = api.get_masteries_by_summoner_id(api.get_summoner_by_name(input())["id"])
    # summoner = api.get_tft_summoner_by_name("moreninha52")
    last_20_matches = api.get_tft_match_by_player_puuid(api.get_tft_summoner_by_name("moreninha52")["puuid"], 20)
    response = api.get_tft_match_by_match_id("BR1_1821009083")
    #print(response)
    #print(last_20_matches)

    #print(response["metadata"])
    #print(response["info"])

    #print(JsonReader.read_tft_champions_static_data())


if __name__ == "__main__":
    main()
