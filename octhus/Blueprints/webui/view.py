from flask import request, jsonify, render_template, redirect, url_for, send_file

#import de funções de retorno
from octhus.extension.animeConfig import push_animes, animeReleases

def index():
	return render_template("index.html")

def releases():
	animes = animeReleases()
	return render_template("releases.html", anime=animes)

def season():
	if request.method == 'POST':
		year = request.form['year']
		season = request.form['season']
		templateAnimes = push_animes(year=int(year),month=season)
		return render_template("season.html", temp=templateAnimes, year=int(year))
	templateAnimes = push_animes()
	return render_template("season.html", temp=templateAnimes, year=2020)

