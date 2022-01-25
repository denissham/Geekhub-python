# Використовуючи бібліотеку requests написати скрейпер для отримання статей / записів із АПІ
# Документація на АПІ:
# https://github.com/HackerNews/API
# Скрипт повинен отримувати із командного рядка одну із наступних категорій:
# askstories, showstories, newstories, jobstories
# Якщо жодної категорії не указано - використовувати newstories.
# Якщо категорія не входить в список - вивести попередження про це і завершити роботу.
# Результати роботи зберегти в CSV файл. Зберігати всі доступні поля. Зверніть увагу - інстанси різних типів мають різний набір полів.
# Код повинен притримуватися стандарту pep8.
# Перевірити свій код можна з допомогою ресурсу http://pep8online.com/
# Для тих, кому хочеться зробити щось "додаткове" - можете зробити наступне: другим параметром cкрипт може приймати
# назву HTML тега і за допомогою регулярного виразу видаляти цей тег разом із усим його вмістом із значення атрибута "text"
# (якщо він існує) отриманого запису.

import requests
import os.path

from csv import DictWriter


class NewsScraper(object):
	def __init__(self):
		helo_text = ("Введіть будь ласка Категорію для пошуку"
		"(askstories, showstories, newstories, jobstories): ") 
		self.category = str(input(helo_text))
		self.availability = self.start(self.category)
		self.category_list = self.get_stories_list()
		self.story = self.get_story()
		self.write = self.write_csv()
	def start(self, category):
		available_category = ['askstories', 'showstories', 'newstories', 'jobstories']
		if len(category) == 0:
			self.category = "newstories"
		elif category not in available_category:
			print("Sorry you entered not available category!")
			exit()
	def get_stories_list(self):
		url = f"https://hacker-news.firebaseio.com/v0/{self.category}.json?print=pretty"
		r = requests.get(url)
		response_value = r.json()
		return response_value
	def get_story(self):
		stories_list = []
		for story in self.category_list:
			story_url = f"https://hacker-news.firebaseio.com/v0/item/{story}.json?print=pretty"
			story_response = requests.get(story_url)
			story_data = story_response.json()
			stories_list.append(story_data)
		return stories_list	
	def write_csv(self):
		file_check = os.path.isfile(f"./{self.category}.csv")
		counter = 1
		headersCSV = ['id', 'deleted', 'type', 'by', 'time', 'text', 'dead',
		'parent', 'poll', 'kids', 'url', 'score', 'title', 'parts', 'descendants']
		print(headersCSV)
		for story in self.story:
			if file_check == True and counter == 1:
				with open(f'{self.category}.csv', 'w', newline='') as f_object:
					dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
					dictwriter_object.writerow(story)
					f_object.close()
				counter += 1
			else:
				with open(f'{self.category}.csv', 'a', newline='') as f_object:
					dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
					dictwriter_object.writerow(story)
					f_object.close()

category_data = NewsScraper()
