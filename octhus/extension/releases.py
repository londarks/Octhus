import requests
from bs4 import BeautifulSoup
import time 


def animeSearch():
	conect = requests.get('https://www.animestc.com')
	soup = BeautifulSoup(conect.text, "lxml")
	animeList = {}
	animeList['name'] = []
	animeList['url'] = []
	animeList['download'] = []

	for i in range(len(soup.find_all('div', {'class': 'tooltip-container'}))):
		download = soup.find_all('div', {'class': 'tooltip-container'})[i].find_all('a', {'class': 'episode-info-links-item episode-info-links-item-blue'})[2]
		animeList['download'].append(download['href'])
		anime = soup.find_all('div', {'class': 'tooltip-container'})[i].find('img',{'class': 'episode-image'})
		animeList['name'].append(anime['alt'])
		animeList['url'].append(anime['data-src'])
		
	return animeList


#animeSearch()

#nome
#print(teste['alt'])

#thumbnail
#print(teste['data-src'])