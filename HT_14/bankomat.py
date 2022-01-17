# 1. Доповніть програму-банкомат наступним функціоналом:
#    - новий пункт меню, який буде виводити поточний курс валют (API Приватбанк)


import csv
import ast
import json
import pickle
import sqlite3

import requests
from texttable import Texttable


import database

class Menu(object):

	def menu(self, username, password, role):

		cash_from_db = database.Database().get_cash()
		cash = {}
		for i in cash_from_db:
			a = i[0]
			b = i[1]
			cash[a]=b
		
		
		if role == "incasator":
			print("""Введіть дію:
				1. Переглянути наявні купюри;
				2. Змінити кількість купюр;
				3. Додати нового користувача;
				""")
			action = int(input())
			if action == 1:
				print("Наявні банкноти в банкоматі: ")
				print(cash)
				answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
				if answer_work == "y":
					self.menu(username, password, role)
				elif answer_work == "n":
					print("Дякуємо, що скористались нашим банкоматом")
					exit()

			elif action == 2:
				atm.adding_cash(username, password, role)

			elif action == 3:
				user_credentials.add_user(username, password, role)


		if role == "user":
			print("""Введіть дію:
	           1. Продивитись баланс
	           2. Поповнити баланс/Зняття коштів
	           3. Курс Валют
	           4. Вихід""")
			action = int(input())

			if action == 1:
				atm.balance_check(username, password, role)

			elif action == 2:
				print("""Введіть дію:
	   				1. Бажаєте внести кошти
	   				2. Бажаєте зняти певну кількіст коштів
	   				3. Повернутись до попереднього меню""")
				balance_change_action = int(input())
				if balance_change_action == 1:
					atm.adding_balance(username, password, role)
				elif balance_change_action == 2:
					atm.withdrawal_balance(cash,username,password, role)
			elif action == 3:
				atm.exchange_rate(username, password, role)

			else:
				exit()

class Bankomat(object):

	def withdrawal_balance(self,cash , username, password, role):
		appendix = int(input("Скільки грошей ви хочете зняти?: "))
		if appendix >= 0:
			if appendix % 10 == 0:
				id_db = database.Database().get_user_id(username)
				balance = database.Database().get_user_balance(id_db)
				result = balance - appendix
				if result < 0:
					print("Ви привисили ліміт!")
					answer = input("Бажаєте змінити сумму зняття коштів(y/n): ")
					if answer == "y":
						self.withdrawal_balance(cash,username,password,role)
					else:
						answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
						if answer_work == "y":
							atm_menu.menu(username, password, role)
						elif answer_work == "n":
							print("Дякуємо, що скористались нашим банкоматом")
							exit()
				elif result >= 0:
					test = self.countCurrency(appendix,username)
					if test == False:
						print("В банкоматі закінчились кошти1")
						answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
						if answer_work == "y":
							atm_menu.menu(username, password, role)
						elif answer_work == "n":
							print("Дякуємо, що скористались нашим банкоматом")
							exit()
					else:
						cash_dict = cash
						temporary_cash_withdraw = {}
						for key, value in test.items():

							if int(cash_dict[str(key)])>=value:
								cash_counter = cash_dict[str(key)]-value
								new_appendix = appendix - (key*value)
								temporary_cash_withdraw[str(key)] = cash_counter
							else:
								break
						
						if len(temporary_cash_withdraw) == len(test):
							cash_dict.update(temporary_cash_withdraw)
							for i,j in cash_dict.items():
								database.Database().update_cash(i, j)
						
						else:
							print("В банкоматі закінчились кошти")
							answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
							if answer_work == "y":
								atm_menu.menu(username, password, role)
							elif answer_work == "n":
								print("Дякуємо, що скористались нашим банкоматом")
								exit()	
									

				database.Database().update_balance(result, id_db)
				text = "Гроші було знято"
				transaction_value = str({text:appendix})
				database.Database().write_transaction(id_db, transaction_value)
				print("Ви отримаєте гроші таких номиналів", test)
				answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
				if answer_work == "y":
					atm_menu.menu(username, password, role)
				elif answer_work == "n":
					print("Дякуємо, що скористались нашим банкоматом")
					exit()

			elif appendix % 10 > 0:
				print("Сумма повинна бути кратна 10")
				answer = input("Бажаєте змінити сумму зняття коштів(y/n): ")
				if answer == "y":
					self.withdrawal_balance(cash, username, password, role)
				else:
					answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
					if answer_work == "y":
						atm_menu.menu(username, password)
					elif answer_work == "n":
						print("Дякуємо, що скористались нашим банкоматом")
						exit()


	def adding_balance(self, username, password, role):
		appendix = int(input("Скільки грошей ви хочете додати?: "))
		if appendix >= 0:
			if appendix % 10 == 0:
				id_db = database.Database().get_user_id(username)
				balance = database.Database().get_user_balance(id_db)
				result = balance + appendix
				database.Database().update_balance(result, id_db)
				text = "Гроші було додано"
				transaction_value = str({text:appendix})
				database.Database().write_transaction(id_db, transaction_value)

				answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
				if answer_work == "y":
					atm_menu.menu(username, password, role)
				elif answer_work == "n":
					print("Дякуємо, що скористались нашим банкоматом")
					exit()
			else:
				print("Сумма повинна бути кратна 10")
				answer = input("Бажаєте змінити суму (y/n): ")
				if answer == "y":
					self.adding_balance(username,password, role)
				elif answer == "n":
					answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
					if answer_work == "y":
						atm_menu.menu(username, password, role)
					elif answer_work == "n":
						print("Дякуємо, що скористались нашим банкоматом")
						exit()
		else:
			print("Ви ввели сумму яка не відповідає данному пункту меню")
			answer = input("Бажаєте змінити суму (y/n): ")
			if answer == "y":
				self.adding_balance(username, password, role)
			elif answer == "n":
				answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
				if answer_work == "y":
					atm_menu.menu(username, password, role)
				elif answer_work == "n":
					print("Дякуємо, що скористались нашим банкоматом")
					exit()


	def balance_check(self, username, password, role):
		id_db = database.Database().get_user_id(username)
		result = database.Database().get_user_balance(id_db)
		print("Ваш баланс: ", result)
		answer = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
		if answer == "y":
			atm_menu.menu(username, password, role)
		else:
			print("Дякуємо, що скористались нашим банкоматом")
			exit()	

	def adding_cash(self,username,password, role):
		cash_from_db = database.Database().get_cash()
		cash = {}

		for i in cash_from_db:
			a = i[0]
			b = i[1]
			cash[a]=b

		banknote= input("Введіть у якої банкноти ви хочете змінити кількість: ")
		banknote_count= int(input("Введіть кількість на яку треба Збільшити/Зменшити кількість банкнот(якщо зменшити введіть від'ємне значення): "))
		if banknote in cash:
			for key, value in cash.items():
				if key == banknote:
					if value + banknote_count>=0:
						result = value + banknote_count
						cash[banknote] = result

						for i,j in cash.items():
							database.Database().update_cash(i, j)

						if banknote_count >= 0:
							text = "Кількість купюр було збільшено"
						else:
							text =  "Кількість купюр було зменшено"

						id_db = database.Database().get_user_id(username)
						transaction_value = str({text:[banknote,banknote_count]})
						database.Database().write_transaction(id_db, transaction_value)

						answer = input("Бажаєте змінити кількість іншої банкноти(y/n): ")
						if answer == "y":
							self.adding_cash(username, password, role)
						elif answer == "n":
							answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
							if answer_work == "y":
								atm_menu.menu(username, password, role)
							elif answer_work == "n":
								print("Дякуємо, що скористались нашим банкоматом")
								exit()
					else:
						print("Kількість зменшенння більша за кількість купюри")
						answer = input("Бажаєте змінити кількість іншої банкноти(y/n): ")
						if answer == "y":
							self.adding_cash(username, password, role)
						elif answer == "n":
							answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
							if answer_work == "y":
								atm_menu.menu(username, password, role)
							elif answer_work == "n":
								print("Дякуємо, що скористались нашим банкоматом")
								exit()
		else:
			print("Ви ввели не існуючу банкноту")
			answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			if answer_work == "y":
				atm_menu.menu(username, password, role)
			elif answer_work == "n":
				print("Дякуємо, що скористались нашим банкоматом")
				exit()
			else:
				exit()

	def countCurrency(self, appendix, username):
		cash_from_db = database.Database().get_cash()
		cash = {}
		for i in cash_from_db:
			a = i[0]
			b = i[1]
			cash[a]=b
		test_notes = []
		for key,value in cash.items():
			if value > 0 :
				test_notes.append(int(key))
		test_notes.reverse()
		notes = test_notes
		note_counter = []
		if len(notes)>0:

			for i in range(len(notes)):
				note_counter.append(0)
			appendix_count = appendix
			test = {}
			key = int
			for i, j in zip(notes, note_counter):
				if appendix_count >= i:
					j = appendix_count // i
					appendix_count = appendix_count - j * i
					test[i]=j
					key = i

			if appendix_count != 0:
				c = test.pop(key)
				notes1 = notes
				noteCounter1 = note_counter
				notes1.remove(key)
				noteCounter1.remove(0)
				sum_notes = appendix
				for i in test:
					sum_notes = sum_notes - (i*test[i])

				for k, z in zip(notes1, noteCounter1):
					if sum_notes >= k:
						z = sum_notes // k
						sum_notes = sum_notes - z * k
						test[k]=z
			return test

		else:
			return False

	def exchange_rate(self, username, password, role):
		url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
		r = requests.get(url)
		response_value = r.text
		response_to_dict = ast.literal_eval(response_value)
		result = [["Валюта", "Покупка", "Продаж"]]
		
		for i in response_to_dict:
			currency_result = []
			for key,value in i.items():
				if key == "ccy":
					currency_result.append(value)
				elif key == "buy":
					currency_result.append(value)
				elif key == "sale":
					currency_result.append(value)
			result.append(currency_result)

		t = Texttable()
		t.add_rows(result)
		print(t.draw())
		answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
		if answer_work == "y":
			atm_menu.menu(username, password, role)
		elif answer_work == "n":
			print("Дякуємо, що скористались нашим банкоматом")
			exit()

class Person(object):

	def start(self):
		username = str(input("Введіть будь ласка Юзернейм: "))
		password = str(input("Введіть будь ласка Пасворд: "))
		return username, password

	def add_user(self, username, password, role):
		new_username = str(input("Введіть будь ласка Юзернейм нового користувача: "))
		new_password = str(input("Введіть будь ласка Пасворд нового користувача: "))
		new_role = str(input("Введіть будь ласка Роль нового користувача: "))
		database.Database().add_new_user(new_username, new_password, new_role)
		answer = input("Бажаєте додати ще одного користувача(y/n): ")
		if answer == "y":
			
			self.add_user(username, password, role)
		elif answer == "n":
			answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			if answer_work == "y":
				atm_menu.menu(username, password, role)
			elif answer_work == "n":
				print("Дякуємо, що скористались нашим банкоматом")
				exit()


class Auth(Person):

	def login(self, username, password):

		try:
			username_db = database.Database().get_username(username)
			password_db = database.Database().get_password(username)
			role_db = database.Database().get_role(username)
			if username == username_db and password == password_db:
				if role_db=="incasator":
					role = role_db
					return role, username, password
				else:
					role = role_db
					return role, username, password
		except Exception as e:
			print("Введені данні не вірні")
			exit()


db = database.Database()
db.data_base_create()

user_credentials = Auth()
a = user_credentials.start()
user = user_credentials.login(a[0],a[1])

atm = Bankomat()
atm_menu = Menu()
atm_menu.menu(user[1], user[2], user[0])




