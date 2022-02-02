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

import sys
import time
import calendar
import requests

from csv import DictWriter


class NewsScraper(object):

	def __init__(self): 
		if len(sys.argv) >= 2:
			self.category = sys.argv[1]
			self.availability = self.start(self.category)
			self.category_list = self.get_stories_list()
			self.story = self.get_story()
			self.write = self.write_csv()
		else:
			self.category = ""
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
		keys_set=set()
		ts = calendar.timegm(time.gmtime())
		for story in self.story:
				for key, value in story.items():
					keys_set.add(key)

		with open(f'{self.category}{ts}.csv', 'a', newline='') as f_object:
			dictwriter_object = DictWriter(f_object, fieldnames=sorted(keys_set))
			dictwriter_object.writeheader()
			for story in self.story:
				dictwriter_object.writerow(story)

		f_object.close()	
		
if __name__ == '__main__':

	category_data = NewsScraper()
   