from RiotAPI import RiotAPI


def main():
    api = RiotAPI("RGAPI-5584e320-d031-45ed-8e81-960fc913b3c9")
    # id = api.get_summoner_by_name(input())["id"]
    # print(id)
    # response = api.get_masteries_by_summoner_id(id)
    api.challengerleagues_Solo_5x5(0)


# for i in response:
#     print(i, "\n\n")


if __name__ == "__main__":
    main()
