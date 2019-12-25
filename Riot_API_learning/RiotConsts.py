URL = {
    "base": "https://{}.api.riotgames.com{}",
    "summoner_by_name": "/lol/summoner/v{}/summoners/by-name/{}",
    "tft_summoner_by_name": "/tft/summoner/v{}/summoners/by-name/{}",
    "tft_matches_by_player_puuid": "/tft/match/v{}/matches/by-puuid/{}/ids",
    "tft_match_by_match_id": "/tft/match/v{}/matches/{}",
    "all_masteries_by_summoner_id": "/lol/champion-mastery/v{}/champion-masteries/by-summoner/{}",
    "challengerleagues": "/lol/league/v4/challengerleagues/by-queue/{}",
}

API_VERSIONS = {
    "champion-mastery": "4",
    "champion": "3",
    "league": "4",
    "lol-status": "3",
    "match": "4",
    "spectator": "4",
    "summoner": "4",
    "third-party-code": "4",
    "tft-league": "1",
    "tft-match": "1",
    "tft-summoner": "1"
}

QUEUES = ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]

REGIONS = {"brasil": "br1"}
