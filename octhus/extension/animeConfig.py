import time, re, requests
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
	conect = requests.get('https://www.animestc.com')
	soup = BeautifulSoup(conect.text, "lxml")
	animeList = {}
	animeList['name'] = []
	animeList['episodes'] = []
	animeList['url'] = []
	animeList['download'] = []

	for i in range(len(soup.find_all('div', {'class': 'tooltip-container'}))):
		download = soup.find_all('div', {'class': 'tooltip-container'})[i].find_all('a', {'class': 'episode-info-links-item episode-info-links-item-blue'})[2]
		animeList['download'].append(download['href'])
		anime = soup.find_all('div', {'class': 'tooltip-container'})[i].find('img',{'class': 'episode-image'})
		
		nameEps = re.findall('-.*', anime['alt'])
		nameAnime = re.findall('.*-', anime['alt'])

		if len(nameAnime[0]) >= 36:
			animeList['name'].append(nameAnime[0][36:])
		else:
			animeList['name'].append(nameAnime[0].replace('-',''))
		animeList['episodes'].append(nameEps[0])
		
		animeList['url'].append(anime['data-src'])
		
	return animeList