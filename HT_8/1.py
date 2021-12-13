# Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
#    Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
#    Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. 
#    P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - 
#    в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  
#    банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).

#    Особливості реалізації:
#    - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
#    - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
#      - переглянути наявні купюри;
#      - змінити кількість купюр;
#    - видача грошей для користувачів відбувається в межах наявних купюр;
#    - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить, 
#    відкладає в окрему касету.

import csv
import json
import pickle

def menu(username, password):
	role = login(username, password)
	with open('cash.data') as f:
		data = f.read()
		cash = json.loads(data)
		f.close()
		

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
			balance_check()

		elif action == 2:
			print("""Введіть дію:
   				1. Бажаєте внести кошти
   				2. Бажаєте зняти певну кількіст коштів
   				3. Повернутись до попереднього меню""")
			balance_change_action = int(input())
			if balance_change_action == 1:
				adding_balance()
			elif balance_change_action == 2:
				withdrawal_balance(cash)

def withdrawal_balance(cash):
	appendix = int(input("Скільки грошей ви хочете зняти?: "))
	if appendix >= 0:
		if appendix % 10 == 0:
			filename_balance = "%s_balance.data" % username
			f = open(filename_balance , 'r')
			balance = int(f.read())
			result = balance - appendix
			if result < 0:
				print("Ви привисили ліміт!")
				answer = input("Бажаєте змінити сумму зняття коштів(y/n): ")
				if answer == "y":
					withdrawal_balance(cash)
				else:
					answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
					if answer_work == "y":
						menu(username, password)
					elif answer_work == "n":
						print("Дякуємо, що скористались нашим банкоматом")
						exit()
			elif result >= 0:
				test = countCurrency(appendix)
				if test == False:
					print("В банкоматі закінчились кошти")
					answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
					if answer_work == "y":
						menu(username, password)
					elif answer_work == "n":
						print("Дякуємо, що скористались нашим банкоматом")
						exit()
				else:

					for key, value in test.items():

						if int(cash[str(key)])>=value:
							cash_counter = cash[str(key)]-value
							cash[str(key)] = cash_counter
							f = open("cash.data", "w")
							json.dump(cash, f)
							f.close()
							new_appendix = appendix - (key*value)
								

			f = open(filename_balance, 'w')
			f.write(str(result))
			f.close()
			text = "Гроші було знято"
			filename_transaction = "%s_transactions.data" % username
			a_dictionary = {text: appendix}
			dict_to_json = json.dumps(a_dictionary)
			encoded_json = str(json.loads(dict_to_json))
			f = open(filename_transaction, 'a')
			f.write(f'\n{encoded_json}')
			f.close()
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
				withdrawal_balance()
			else:
				answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
				if answer_work == "y":
					menu(username, role)
				elif answer_work == "n":
					print("Дякуємо, що скористались нашим банкоматом")
					exit()


def adding_balance():
	appendix = int(input("Скільки грошей ви хочете додати?: "))
	if appendix >= 0: 
		if appendix % 10 == 0:
			filename_balance = "%s_balance.data" % username
			f = open(filename_balance , 'r')
			balance = int(f.read())
			result = balance + appendix
			f = open(filename_balance, 'w')
			f.write(str(result))
			f.close()
				
			text = "Гроші було додано"
			filename_transaction = "%s_transactions.data" % username
			a_dictionary = {text: appendix}
			dict_to_json = json.dumps(a_dictionary)
			encoded_json = str(json.loads(dict_to_json))
			f = open(filename_transaction, 'a')
			f.write(f'\n{encoded_json}')
			f.close()	

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
				adding_balance()
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
			adding_balance()
		elif answer == "n":
			answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			if answer_work == "y":
				menu(username, password)
			elif answer_work == "n":
				print("Дякуємо, що скористались нашим банкоматом")
				exit()


def balance_check():
	filename = "%s_balance.data" % username
	f = open(filename , 'r')
	result = f.read()
	print("Ваш баланс: ", result)
	f.close()
	answer = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
	if answer == "y":
		menu(username, password)
	else:
		print("Дякуємо, що скористались нашим банкоматом")
		exit()	

def adding_cash(cash, username):
	banknote= input("Введіть у якої банкноти ви хочете змінити кількість: ")
	banknote_count= int(input("Введіть кількість на яку треба Збільшити/Зменшити кількість банкнот(якщо зменшити введіть від'ємне значення): "))
	if banknote in cash:
		for key, value in cash.items():
			if key == banknote:
				result = value + banknote_count
				cash[banknote] = result
				f = open("cash.data", "w")
				json.dump(cash, f)
				f.close()
				if banknote_count >= 0:
					text = "Кількість купюр було збільшено"
				else:
					text =  "Кількість купюр було зменшено"

				filename_transaction = "%s_transactions.data" % username
				a_dictionary = {text: [banknote,banknote_count]}
				dict_to_json = json.dumps(a_dictionary)
				encoded_json = str(json.loads(dict_to_json))
				f = open(filename_transaction, 'a')
				f.write(f'\n{encoded_json}')
				f.close()

				answer = input("Бажаєте змінити кількість іншої банкноти(y/n): ")
				if answer == "y":
					f = open("cash.data" , 'r')
					cash = f.read()
					f.close()
					adding_cash(cash, username)
				elif answer == "n":
					answer_work = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
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

	with open("users.data", "r") as f:
		reader = csv.reader(f, delimiter=",")

		for line in reader:
			role = str

			if username == line[0] and password == line[1]:
				if line[2]=="incasator":
					role = line[2]
					return role
				else:
					role = line[2]
					return role
		f.close()

def countCurrency(appendix):
	with open('cash.data') as f:
		data = f.read()
		cash = json.loads(data)
		f.close()
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

username = str(input("Введіть будь ласка Юзернейм: "))
password = str(input("Введіть будь ласка Пасворд: "))

print(menu(username, password))		

