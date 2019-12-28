import requests

import RiotConsts as Consts


class RiotAPI(object):
    def __init__(self, api_key, region=Consts.REGIONS["brasil"]):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {"api_key": self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value

        response = requests.get(
            Consts.URL["base"].format(self.region, api_url), params=args
        )
        return response.json()

    def _request_tft_matches(self, api_url, count=1, params={}):
        args = {"api_key": self.api_key, "count": count}
        for key, value in params.items():
            if key not in args:
                args[key] = value

        response = requests.get(
            Consts.URL["base"].format(
                Consts.REGIONS["americas"], api_url), params=args
        )
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL["summoner_by_name"].format(
            Consts.API_VERSIONS["summoner"], name
        )
        return self._request(api_url)

    def get_tft_summoner_by_name(self, name):
        api_url = Consts.URL["tft_summoner_by_name"].format(
            Consts.API_VERSIONS["tft-summoner"], name
        )
        return self._request(api_url)

    def get_tft_match_by_player_puuid(self, puuid, count=1):
        api_url = Consts.URL["tft_matches_by_player_puuid"].format(
            Consts.API_VERSIONS["tft-match"], puuid
        )
        return self._request_tft_matches(api_url, count)

    def get_tft_match_by_match_id(self, match_id):
        api_url = Consts.URL["tft_match_by_match_id"].format(
            Consts.API_VERSIONS["tft-match"], match_id
        )
        return self._request_tft_matches(api_url)

    # noinspection SpellCheckingInspection
    def get_masteries_by_summoner_id(self, summoner_id):
        api_url = Consts.URL["all_masteries_by_summoner_id"].format(
            Consts.API_VERSIONS["champion-mastery"], summoner_id
        )
        return self._request(api_url)

    def challenger_leagues_solo_5x5(self, queue):
        api_url = Consts.URL["challengerleagues"].format(Consts.QUEUES[0])
        return self._request(api_url)

    def challenger_leagues_flex_sr(self, queue):
        api_url = Consts.URL["challengerleagues"].format(Consts.QUEUES[1])
        return self._request(api_url)

    # def challengerleagues_Flex_TT(self, queue):
    #     api_url = Consts.URL["challengerleagues"].format(Consts.QUEUES[2])
    #     return self._request(api_url)
