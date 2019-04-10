import RiotConsts as Consts
import requests

class RiotAPI(object):
	def __init__(self, api_key, region=Consts.REGIONS['brasil']):
		self.api_key = api_key
		self.region = region

	def _request(self, api_url, params={}):
		args = {'api_key': self.api_key}
		for key, value in params.items():
			if key not in args:
				args[key] = value

		response = requests.get(
			Consts.URL['base'].format(self.region, api_url),
			params = args
			)
		print(response.url)
		return response.json()

	def get_summoner_by_name(self, name):
		api_url = Consts.URL['summoner_by_name'].format(Consts.API_VERSIONS['summoner'], name)
		return self._request(api_url)


	def get_masteries_by_summoner_id(self, summoner_id):
		api_url = Consts.URL['all_masteries_by_summoner_id'].format(Consts.API_VERSIONS['champion-mastery'], summoner_id)
		return self._request(api_url)