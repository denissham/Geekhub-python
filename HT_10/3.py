# 3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
#    Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
#    конвертацію введеної суми з однієї валюти в іншу.
# P.S. Не забувайте про файл requirements.txt
# P.P.S. Не треба сходу ДДОСить Приватбанк - додайте хоча б по 0.5 секунди між запросами.
#        Хоч у них і не написано за троттлінг, але будьмо чемними ;)
# Інформація для виконання:
# - документація API Приватбанка:
#   - архів курсів: https://api.privatbank.ua/#p24/exchangeArchive
#   - поточний курс: https://api.privatbank.ua/#p24/exchange
# - інформація про використання форматування дати в Python: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# - модуль requests: https://docs.python-requests.org/en/latest/

import requests
import ast
from datetime import datetime
from datetime import timedelta, date

def calculation(amount, sale_rate_one, sale_rate_two):
	koefficient = sale_rate_one/sale_rate_two
	result = amount*koefficient
	return result

def converter():
	currency_one = input("""Введіть валюту історію курсу якої ви б хотіли подивитись(доступні валюти:AUD,CAD,CZK,DKK,HUF,ILS,JPY,LVL,LTL
		NOK,SKK,SEK,CHF,RUB,GBP,USD,BYR,EUR,GEL,PLN): """)
	amount = int(input("Введіть сумму яку ви б хотіли обміняти: "))
	currency_two = input("""Введіть валюту історію курсу якої ви б хотіли подивитись(доступні валюти:AUD,CAD,CZK,DKK,HUF,ILS,JPY,LVL,LTL
		NOK,SKK,SEK,CHF,RUB,GBP,USD,BYR,EUR,GEL,PLN): """)

	available_currencies = ["AUD", "CAD", "CZK", "DKK", "HUF", "ILS", "JPY", "LVL", "LTL",
		"NOK" , "SKK", "SEK", "CHF", "RUB", "GBP", "USD", "BYR", "EUR", "GEL", "PLN"]
	if currency_one in available_currencies and currency_two in available_currencies:
		date_current = datetime.today()
		datex=date_current.strftime("%Y-%m-%d")
		x = datex.split("-")
		year = int(x[0])
		month = int(x[1])
		day = int(x[2])
		dt = date(year, month, day)
		dt_formated = dt.strftime("%d.%m.%Y")
		url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={dt_formated}"
		r = requests.get(url)
		response_value = r.text
		response_to_dict = ast.literal_eval(response_value)
		rates = response_to_dict['exchangeRate']
		if len(rates)==0:
			dt_yesterday = dt - timedelta(days=1)
			dt_yesterday_formated = dt_yesterday.strftime("%d.%m.%Y")
			url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={dt_yesterday_formated}"
			r = requests.get(url)
			response_value = r.text
			response_to_dict = ast.literal_eval(response_value)
			rates = response_to_dict['exchangeRate']
			sale_rate_one = float
			sale_rate_two = float
			for i in rates:
				if 'currency' in i:
					if i['currency'] == currency_one:
						sale_rate_one = i["saleRateNB"]
					elif i['currency'] == currency_two:
						sale_rate_two = i["saleRateNB"]
			calculated_result = calculation(amount, sale_rate_one, sale_rate_two)
			calculated_round_result = round(calculated_result, 2)
			print(f" Ви хочете обміняти {amount} {currency_one} на {currency_two}")
			print(f"Ви отримаєте: {calculated_round_result} {currency_two}")

		else:
			sale_rate_one = float
			sale_rate_two = float
			for i in rates:
				if 'currency' in i:
					if i['currency'] == currency_one:
						sale_rate_one = i["saleRateNB"]
					elif i['currency'] == currency_two:
						sale_rate_two = i["saleRateNB"]
			calculated_result = calculation(amount, sale_rate_one, sale_rate_two)
			calculated_round_result = round(calculated_result, 2)
			print(f" Ви хочете обміняти {amount} {currency_one} на {currency_two}")
			print(f"Ви отримаєте: {calculated_round_result} {currency_two}")
	else:
            print("You entered currency which i`m not working with")

converter()