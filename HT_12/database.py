import sqlite3
from pathlib import Path

def data_base_create():
	con = sqlite3.connect(Path(__file__).parent/ 'quotes.db')
	cur = con.cursor()
	cur.execute('''
	CREATE TABLE IF NOT EXISTS authors (
		id integer PRIMARY KEY AUTOINCREMENT,
		author text NOT NULL,
		born_date text NOT NULL,
		born_location text NOT NULL,
		descritption text NOT NULL,
		UNIQUE(author)
	);
	''')

	cur.execute('''
	CREATE TABLE IF NOT EXISTS quotes (
		author_id integer,
		quote_text text NOT NULL,
		UNIQUE(quote_text)
		FOREIGN KEY (author_id) REFERENCES authors (id)
	);
	''')