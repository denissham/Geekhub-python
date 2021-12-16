# Перепишіть програму-банкомат на використання бази даних для збереження всих даних.
# Використовувати БД sqlite3 та натівний Python.
# Дока з прикладами: https://docs.python.org/3/library/sqlite3.html
# Туторіал (один із): https://www.sqlitetutorial.net/sqlite-python/
# Для уніфікації перевірки, в базі повинні бути 3 користувача:
#   ім'я: user1, пароль: user1
#   ім'я: user2, пароль: user2
#   ім'я: admin, пароль: admin (у цього коритувача - права інкасатора)
import sqlite3
import csv
import json
import pickle
import ast
import database

database.data_base_create()

def start():
	username = str(input("Введіть будь ласка Юзернейм: "))
	password = str(input("Введіть будь ласка Пасворд: "))
	menu(username, password)

def menu(username, password):

	role = login(username, password)
	con = sqlite3.connect("bankomat.db")
	cursor = con.cursor()
	cursor.execute("SELECT banknotes FROM cash WHERE id ==1")
	cash = cursor.fetchall()[0][0]
	con.close()
	
	if role == "incasator":
		print("""Введіть дію:
			1.переглянути наявні купюри;
			2.змінити кількість купюр;""")
		action = int(input())
		if action == 1:
			print("Наявні банкноти в банкоматі: ")
			print(cash)
			answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			if answer_work == "y":
				menu(username, password)
			elif answer_work == "n":
				print("Дякуємо, що скористались нашим банкоматом")
				exit()

		elif action == 2:
			adding_cash(cash, username)

	if role == "user":
		print("""Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс/Зняття коштів
           3. Вихід""")
		action = int(input())

		if action == 1:
			balance_check(username,password)

		elif action == 2:
			print("""Введіть дію:
   				1. Бажаєте внести кошти
   				2. Бажаєте зняти певну кількіст коштів
   				3. Повернутись до попереднього меню""")
			balance_change_action = int(input())
			if balance_change_action == 1:
				adding_balance(username,password)
			elif balance_change_action == 2:
				withdrawal_balance(cash,username,password)

def withdrawal_balance(cash,username,password):
	appendix = int(input("Скільки грошей ви хочете зняти?: "))
	if appendix >= 0:
		if appendix % 10 == 0:
			con = sqlite3.connect("bankomat.db")
			cursor = con.cursor()
			cursor.execute(f"SELECT id FROM users WHERE username LIKE \"%{username}%\";")
			id_db = cursor.fetchall()[0][0]
			cursor.execute(f"SELECT amount FROM balance WHERE user_id LIKE \"%{id_db}%\";")
			balance = cursor.fetchall()[0][0]
			result = balance - appendix
			if result < 0:
				print("Ви привисили ліміт!")
				answer = input("Бажаєте змінити сумму зняття коштів(y/n): ")
				if answer == "y":
					withdrawal_balance(cash,username)
				else:
					answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
					if answer_work == "y":
						menu(username, password)
					elif answer_work == "n":
						print("Дякуємо, що скористались нашим банкоматом")
						exit()
			elif result >= 0:
				test = countCurrency(appendix,username)
				if test == False:
					print("В банкоматі закінчились кошти1")
					answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
					if answer_work == "y":
						menu(username, password)
					elif answer_work == "n":
						print("Дякуємо, що скористались нашим банкоматом")
						exit()
				else:
					cash_dict = ast.literal_eval(cash)
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
						cursor.execute(f"UPDATE cash SET banknotes = \"{cash_dict}\" WHERE id == 1")
						con.commit()
					
					else:
						print("В банкоматі закінчились кошти")
						answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
						if answer_work == "y":
							menu(username, password)
						elif answer_work == "n":
							print("Дякуємо, що скористались нашим банкоматом")
							exit()	
								

			cursor.execute(f"UPDATE balance SET amount = \"{result}\" WHERE user_id == \"{id_db}\"")
			con.commit()
			text = "Гроші було знято"
			transaction_value = str({text:appendix})
			cursor.execute("INSERT INTO transactions (user_id,text_transaction) VALUES (?,?)", (id_db,transaction_value))
			con.commit()
			con.close()
			print("Ви отримаэте гроші таких номиналів", test)
			answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			if answer_work == "y":
				menu(username, password)
			elif answer_work == "n":
				print("Дякуємо, що скористались нашим банкоматом")
				exit()

		elif appendix % 10 > 0:
			print("Сумма повинна бути кратна 10")
			answer = input("Бажаєте змінити сумму зняття коштів(y/n): ")
			if answer == "y":
				withdrawal_balance(cash,username)
			else:
				answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
				if answer_work == "y":
					menu(username, password)
				elif answer_work == "n":
					print("Дякуємо, що скористались нашим банкоматом")
					exit()


def adding_balance(username,password):
	appendix = int(input("Скільки грошей ви хочете додати?: "))
	if appendix >= 0:
		if appendix % 10 == 0:
			con = sqlite3.connect("bankomat.db")
			cursor = con.cursor()
			cursor.execute(f"SELECT id FROM users WHERE username LIKE \"%{username}%\";")
			id_db = cursor.fetchall()[0][0]
			cursor.execute(f"SELECT amount FROM balance WHERE user_id LIKE \"%{id_db}%\";")
			balance = cursor.fetchall()[0][0]
			result = balance + appendix
			cursor.execute(f"UPDATE balance SET amount = \"{result}\" WHERE user_id == \"{id_db}\"")
			con.commit()
			text = "Гроші було додано"
			transaction_value = str({text:appendix})
			cursor.execute("INSERT INTO transactions (user_id,text_transaction) VALUES (?,?)", (id_db,transaction_value))
			con.commit()
			con.close()

			answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			if answer_work == "y":
				menu(username, password)
			elif answer_work == "n":
				print("Дякуємо, що скористались нашим банкоматом")
				exit()
		else:
			print("Сумма повинна бути кратна 10")
			answer = input("Бажаєте змінити суму (y/n): ")
			if answer == "y":
				adding_balance(username,password)
			elif answer == "n":
				answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
				if answer_work == "y":
					menu(username, password)
				elif answer_work == "n":
					print("Дякуємо, що скористались нашим банкоматом")
					exit()
	else:
		print("Ви ввели сумму яка не відповідає данному пункту меню")
		answer = input("Бажаєте змінити суму (y/n): ")
		if answer == "y":
			adding_balance(username,password)
		elif answer == "n":
			answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			if answer_work == "y":
				menu(username, password)
			elif answer_work == "n":
				print("Дякуємо, що скористались нашим банкоматом")
				exit()


def balance_check(username,password):
	con = sqlite3.connect("bankomat.db")
	cursor = con.cursor()
	cursor.execute(f"SELECT id FROM users WHERE username LIKE \"%{username}%\";")
	id_db = cursor.fetchall()[0][0]
	cursor.execute(f"SELECT amount FROM balance WHERE user_id LIKE \"%{id_db}%\";")
	result = cursor.fetchall()[0][0]
	con.close()
	print("Ваш баланс: ", result)
	answer = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
	if answer == "y":
		menu(username, password)
	else:
		print("Дякуємо, що скористались нашим банкоматом")
		exit()	

def adding_cash(cash, username):
	con = sqlite3.connect("bankomat.db")
	cursor = con.cursor()
	cursor.execute("SELECT banknotes FROM cash WHERE id ==1")
	str_cash = cursor.fetchall()[0][0]
	cash = ast.literal_eval(str_cash)

	
	banknote= input("Введіть у якої банкноти ви хочете змінити кількість: ")
	banknote_count= int(input("Введіть кількість на яку треба Збільшити/Зменшити кількість банкнот(якщо зменшити введіть від'ємне значення): "))
	if banknote in cash:
		for key, value in cash.items():
			if key == banknote:
				result = value + banknote_count
				cash[banknote] = result

				cursor.execute(f"UPDATE cash SET banknotes = \"{cash}\" WHERE id == 1")
				con.commit()
				if banknote_count >= 0:
					text = "Кількість купюр було збільшено"
				else:
					text =  "Кількість купюр було зменшено"

				cursor.execute(f"SELECT id FROM users WHERE username LIKE \"%{username}%\";")
				id_db = int(cursor.fetchall()[0][0])
				transaction_value = str({text:[banknote,banknote_count]})

				print(transaction_value)
				cursor.execute("INSERT INTO transactions (user_id,text_transaction) VALUES (?,?)", (id_db,transaction_value))
				con.commit()

				answer = input("Бажаєте змінити кількість іншої банкноти(y/n): ")
				if answer == "y":
					cursor.execute("SELECT banknotes FROM cash WHERE id ==1")
					str_cash = cursor.fetchall()[0][0]
					cash = ast.literal_eval(str_cash)
					con.close()
					adding_cash(cash, username)
				elif answer == "n":
					answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
					con.close()
					if answer_work == "y":
						menu(username, password)
					elif answer_work == "n":
						print("Дякуємо, що скористались нашим банкоматом")
						exit()
	else:
		print("Ви ввели не існуючу банкноту")
		answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
		if answer_work == "y":
				menu(username, role)
		elif answer_work == "n":
			print("Дякуємо, що скористались нашим банкоматом")
			exit()
		else:
			exit()



def login(username, password):
	con = sqlite3.connect("bankomat.db")
	cursor = con.cursor()
	try:
		cursor.execute(f"SELECT username FROM users WHERE username LIKE \"%{username}%\";")
		username_db = cursor.fetchall()[0][0]
		cursor.execute(f"SELECT password FROM users WHERE username LIKE \"%{username}%\";")
		password_db = cursor.fetchall()[0][0]
		cursor.execute(f"SELECT role FROM users WHERE username LIKE \"%{username}%\";")
		role_db = cursor.fetchall()[0][0]
		if username == username_db and password == password_db:
			if role_db=="incasator":
				role = role_db
				return role
			else:
				role = role_db
				return role
	except Exception as e:
		print("Введені данні не вірні")

	con.commit()
	con.close()

def countCurrency(appendix,username):
	con = sqlite3.connect("bankomat.db")
	cursor = con.cursor()
	cursor.execute("SELECT banknotes FROM cash WHERE id ==1")
	str_cash = cursor.fetchall()[0][0]
	cash = ast.literal_eval(str_cash)
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

start()