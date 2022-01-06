#    http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
#    цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу. Результати зберегти в репозиторії.
#    Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL). Хто захардкодить
#    пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)

import requests
from bs4 import BeautifulSoup
import sqlite3
import database
import csv
from csv import DictWriter

database.data_base_create()

def get_quotes(url):
	con = sqlite3.connect("quotes.db")
	cursor = con.cursor()
	page_response = requests.get(f'http://quotes.toscrape.com{url}')
	soup = BeautifulSoup(page_response.text, 'lxml')
	quotes = soup.select('.quote')
	headersCSV = ["Quote",'Author',"Author_Born_Date", "Author_Born_Location","Author_Description"]
	for i in quotes:
		quote = i.select_one('.text')
		author_section = i.select_one('.author')
		author = author_section.text
		cursor.execute(f"SELECT id FROM authors WHERE author LIKE \"%{author}%\";")
		id_db = cursor.fetchall()
		if len(id_db)==0:
			link = i.select_one('a')
			author_link = link.get('href')
			author_page_response = requests.get(f'http://quotes.toscrape.com/{author_link}')
			soup_author = BeautifulSoup(author_page_response.text, 'lxml')
			author_born_date = soup_author.select_one('.author-born-date')
			author_born_location = soup_author.select_one('.author-born-location')
			author_description = soup_author.select_one('.author-description')
			cursor.execute("INSERT OR IGNORE INTO authors (author, born_date, born_location, descritption) VALUES (?,?,?,?)", 
			(author, author_born_date.text, author_born_location.text, author_description.text))
			con.commit()
			cursor.execute(f"SELECT id FROM authors WHERE author LIKE \"%{author}%\";")
			id_db = cursor.fetchall()[0][0]
			cursor.execute("INSERT OR IGNORE INTO quotes (author_id, quote_text) VALUES (?,?)", (id_db, quote.text))
			con.commit()
			dict={"Quote":quote.text ,"Author":author,"Author_Born_Date":author_born_date.text, "Author_Born_Location":author_born_location.text,
			"Author_Description":author_description.text}

			with open('QuotesCSV.csv', 'a', newline='') as f_object:
				dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
				dictwriter_object.writerow(dict)
				f_object.close()
		
		else:
			cursor.execute(f"SELECT id FROM authors WHERE author LIKE \"%{author}%\";")
			id_db = cursor.fetchall()[0][0]
			cursor.execute(f"SELECT author, born_date, born_location, descritption FROM authors WHERE author LIKE \"%{author}%\";")
			author_data = cursor.fetchall()[0]
			author_born_date = author_data[1]
			author_born_location = author_data[2]
			author_description = author_data[3]
			cursor.execute("INSERT OR IGNORE INTO quotes (author_id, quote_text) VALUES (?,?)", (id_db, quote.text))
			con.commit()
			dict={"Quote":quote.text ,"Author":author,"Author_Born_Date":author_born_date, "Author_Born_Location":author_born_location,
			"Author_Description":author_description}

			with open('QuotesCSV.csv', 'a', newline='') as f_object:
				dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
				dictwriter_object.writerow(dict)
				f_object.close()

	try:
		next_section = soup.select_one('.next')
		next_a_section = next_section.select_one('a[href]')
		next_link  = next_a_section.get('href')
		if len(next_section)>0:
			get_quotes(next_link)
	except AttributeError:
		exit()


url = ''

get_quotes(url)