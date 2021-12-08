# Програма-банкомат.
#    Створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#       - потім - елементарне меню типа:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив :)

import csv
import json

def start():
	username = str(input("Введіть будь ласка Юзернейм: "))
	password = str(input("Введіть будь ласка Пасворд: "))

	login(username, password)

	if login(username,password) == True:
		menu(username)
	else:
		print("Ви ввели не вірні данні користувача")
		exit()


def login(username, password):

	with open("users.data", "r") as f:
		reader = csv.reader(f, delimiter=",")

		for line in reader:

				if username == line[0] and password == line[1]:
					return True
		f.close()

def menu(username):
	print("""Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс/Зняття коштів
           3. Вихід""")

	action = int(input())
	if action == 1:
		def balance_check():
			filename = "%s_balance.data" % username
			f = open(filename , 'r')
			result = f.read()
			print("Ваш баланс: ", result)
			f.close()
			answer = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			if answer == "y":
				menu(username)
			else:
				print("Дякуємо, що скористались нашим банкоматом")
				exit()

		balance_check()

	elif action == 2:

		def balance_change():
			appendix = int(input("Скільки грошей ви хочете додати?(Якщо хочете зняти кошти введіть негативну сумму): "))
			filename_balance = "%s_balance.data" % username
			f = open(filename_balance , 'r')
			balance = int(f.read())
			result = balance + appendix
			if result < 0:
				print("Ви привисили ліміт!")
				answer = input("Бажаєте змінити сумму зняття коштів(y/n): ")
				if answer == "y":
					balance_change()
				else:
					menu(username)
			f = open(filename_balance, 'w')
			f.write(str(result))
			f.close()

			filename_transaction = "%s_transactions.data" % username

			if appendix >= 0:
				text = "Гроші було додано"
			else:
				text =  "Гроші було знято"

			a_dictionary = {text: appendix}
			dict_to_json = json.dumps(a_dictionary)
			encoded_json = str(json.loads(dict_to_json))
			f = open(filename_transaction, 'a')
			f.write(f'\n{encoded_json}')
			f.close()
			print("Дякуємо Ваш баланс було змінено!")
			answer = input("Бажаєте продовжити роботу з банкоматом(y/n): ")
			
			if answer == "y":
				menu(username)
			else:
				print("Дякуємо, що скористались нашим банкоматом")
				exit()

		balance_change()

	else:
		print("Дякуємо, що скористались нашим банкоматом")
		exit()


start()

# ------------------------------------------------
# Adding users and password

# data = ['admin','admin']
# data_two = ['user','user']
# data_three = ['test','test']


# f = open("users.data", "w")
# writer = csv.writer(f)
# writer.writerow(data)
# writer.writerow(data_two)
# writer.writerow(data_three)
# f.close()

# --------------------------------------------------
# Adding balance to users

# with open('user_balance.data', 'w') as f:
# 	f.write('100')
# 	f.close()

# with open('admin_balance.data', 'w') as f:
# 	f.write('200')
# 	f.close()

# with open('test_balance.data', 'w') as f:
# 	f.write('200')
# 	f.close()