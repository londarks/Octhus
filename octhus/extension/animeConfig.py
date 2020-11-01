import time, re, requests, json
from jikanpy import Jikan
from bs4 import BeautifulSoup


def push_animes(year=2020, month='winter'):
	jikan = Jikan()
	seaasonAnimes = jikan.season(year=year, season=month)
	Animes = {}
	Animes['name'] = []
	Animes['url'] = []
	Animes['rank'] = []
	Animes['eps'] = []

	for i in range(len(seaasonAnimes['anime'])):

		Animes['name'].append(seaasonAnimes['anime'][i]['title'])
		Animes['url'] .append(seaasonAnimes['anime'][i]['image_url'])
		if seaasonAnimes['anime'][i]['score'] == None:
			Animes['rank'].append("???")
		else:
			Animes['rank'].append(seaasonAnimes['anime'][i]['score'])

		if seaasonAnimes['anime'][i]['episodes'] == None:
			Animes['eps'].append("???")
		else:
			Animes['eps'].append(seaasonAnimes['anime'][i]['episodes'])
	return Animes



def animeReleases():
	page = 1
	animeList = {}
	animeList['name'] = []
	animeList['episodes'] = []
	animeList['url'] = []

	for a in range(5):

		params = (
			('order', 'created_at'),
			('direction', 'desc'),
			('page', page),
			('ignoreIndex', 'false'),
			)
		response = requests.get('https://api2.animestc.com/episodes', params=params)
		api = response.json()
		for i in range(len(api['data'])):
			url = 'https://stc.animestc.com/{}'.format(api['data'][i]['cover']['thumbnailName'])
			if len(api['data'][i]['series']['slug']) >= 35:
				name = "{}...".format(api['data'][i]['series']['slug'][:30])
				animeList['name'].append(name)
			else:
				animeList['name'].append(api['data'][i]['series']['slug'])
			episodio = "Episodio {}".format(api['data'][i]['number'])
			animeList['episodes'].append(episodio)

			animeList['url'].append(url)
		page += 1
		
	return animeList