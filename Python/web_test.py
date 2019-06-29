import urllib.request
import urllib.parse
from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup


def sort_all_champ_data(param, data):
    """
    Parameters that can be passed:
    - 1 --> win ratio
    - 2 --> played games (number of games)
    """
    return sorted(data, key=lambda x: x[param], reverse=True)


try:
    champion_name = input()
    lane = input()
    url = "https://br.op.gg/champion/{}/statistics/{}/matchup".format(
        champion_name, lane)
    response = requests.get(url)

    soup_opgg = BeautifulSoup(response.content, "html.parser")

    all_champions_divs = soup_opgg.find_all(
        "div", class_="champion-matchup-champion-list__item"
    )

    all_champ_data = []
    for champ in all_champions_divs:
        champ_spans = champ.find_all(["span", "small"])
        # print(champ_spans)
        champ_data = []
        for i in champ_spans:
            champ_soup = BeautifulSoup(i.text, "html.parser")
            champ_data.append(str(champ_soup))
        all_champ_data.append(champ_data)

    for champ in all_champ_data:
        champ[1] = "".join(
            filter(lambda x: x.isdigit() or x in [".", ",", "%"], champ[1])
        )

    # sorted by win ratio %
    all_champ_data = sort_all_champ_data(1, all_champ_data)
    for champ in all_champ_data:
        print(
            "{} wins {} games against {}. Played games: {} -- {} of total ammount".format(
                champion_name, champ[1], champ[0], champ[3], champ[2]
            )
        )
    print('_' * 200)

    # sorted by number of games
    all_champ_data = sort_all_champ_data(2, all_champ_data)
    for champ in all_champ_data:
        print(
            "{} wins {} games against {}. Played games: {} -- {} of total ammount".format(
                champion_name, champ[1], champ[0], champ[3], champ[2]
            )
        )

    # print("".join(champ_spans.strings))

    # print("champion: {}".format())

    # print(soup.find_all("a"))

except Exception as e:
    print(str(e))
