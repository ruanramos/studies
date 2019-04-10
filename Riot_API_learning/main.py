from RiotAPI import RiotAPI

def main():
	api = RiotAPI('RGAPI-33bd1a06-93f4-4855-82f1-2957bd02169e')
	id = api.get_summoner_by_name(input())['id']
	print(id)
	response = api.get_masteries_by_summoner_id(id)
	for i in response:
		print(i, '\n\n')
	

	

if __name__ == '__main__':
	main()