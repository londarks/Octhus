import sqlite3
import os

def create_Databse():
	conn = sqlite3.connect('Database/Database.db')
	cursor = conn.cursor()
	cursor.execute("""
	CREATE TABLE clientes (
	        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	        nome TEXT NOT NULL,
	        username TEXT NOT NULL,
	        password INTEGER NOT NULL,
	        acess INTEGER NOT NULL,
	        email TEXT NOT NULL,
	        criado_em DATE NOT NULL
	);
	""")
	conn.close()

def load_Database():
	if not os.path.isfile('Database/Database.db'):
		create_Databse()

def init_app(app):
	load_Database()
