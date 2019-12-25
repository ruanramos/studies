import json


def read_tft_champions_static_data():
    champions = []
    with open("champions.json") as f:
        champions_data = json.load(f)
        for champion in champions_data:
            champions.append(champion)
    return champions


def read_tft_traits_static_data():
    traits = []
    with open("traits.json") as t:
        traits_data = json.load(t)
        for trait in traits_data:
            traits.append(trait)
    return traits


def read_tft_items_static_data():
    items = []
    with open("items.json") as i:
        items_data = json.load(i)
        for item in items_data:
            items.append(item)
    return items


def read_tft_hexes_static_data():
    hexes = []
    with open("hexes.json") as f:
        hexes_data = json.load(f)
        for hexes in hexes_data:
            hexes.append(hexes)
    return hexes


def write_json(data, json_file):
    with open(json_file, 'w') as outfile:
        outfile.write(json.dumps(data, indent=4))