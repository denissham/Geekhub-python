# 2. Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
#    - Перелік валют краще принтануть.
#    - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
#    - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
#    - Також перевірте, чи введена правильна валюта.
#    Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
#    курсу обраної валюти (Нацбанк) від введеної дати до поточної. Приблизний вивід наступний:
#    Currency: USD
#    Date: 12.12.2021
#    NBU:  27.1013   -------
#    Date: 13.12.2021
#    NBU:  27.0241   -0,0772
#    Date: 14.12.2021
#    NBU:  26.8846   -0,1395
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
# Свернуть

import requests
import ast
from datetime import datetime
from datetime import timedelta, date

def excahge_rate_library():
    start_input = input("Введіть дату старту в форматі YYYY-MM-DD: ")
    currency = input("""Введіть валюту історію курсу якої ви б хотіли подивитись(доступні валюти:AUD,CAD,CZK,DKK,HUF,ILS,JPY,LVL,LTL
        NOK,SKK,SEK,CHF,RUB,GBP,USD,BYR,EUR,GEL,PLN): """)
    available_currencies = ["AUD", "CAD", "CZK", "DKK", "HUF", "ILS", "JPY", "LVL", "LTL",
     "NOK" , "SKK", "SEK", "CHF", "RUB", "GBP", "USD", "BYR", "EUR", "GEL", "PLN"]
    x = start_input.split("-")
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])
    start_dt = date(year, month, day)
    end_date = datetime.today()
    end_datex=end_date.strftime("%Y-%m-%d")
    end_x = end_datex.split("-")
    end_year = int(end_x[0])
    end_month = int(end_x[1])
    end_day = int(end_x[2])
    end_dt = date(end_year, end_month, end_day)

    if start_dt <= end_dt:
        if currency in available_currencies:
            print(f"Currency:   {currency}")
            previous_value = float(0)

            for dt in daterange(start_dt, end_dt):
                print(dt.strftime("%d.%m.%Y"))
                dt_formated = dt.strftime("%d.%m.%Y")
                url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={dt_formated}"
                r = requests.get(url)
                response_value = r.text
                response_to_dict = ast.literal_eval(response_value)
                rates = response_to_dict['exchangeRate']
                for i in rates:
                    if 'currency' in i:
                        if i['currency'] == currency:
                            sale_rate = i["saleRateNB"]
                            diff = i["saleRateNB"] - previous_value
                            diff_round = round(diff, 4)
                            
                            if diff_round == 0 or previous_value == 0:
                                previous_value = sale_rate
                                print(f"DATE:  {dt_formated}")
                                print(f"NBU:   {sale_rate}      {'---'}")
                            elif diff_round > 0:
                                previous_value = sale_rate
                                print(f"DATE:  {dt_formated}")
                                print(f"NBU:   {sale_rate}      {diff_round}")
                            elif diff_round < 0:
                                previous_value = sale_rate
                                print(f"DATE:  {dt_formated}")
                                print(f"NBU:   {sale_rate}      {diff_round}")
        else:
            print("You entered currency which i`m not working with")
    else:
        print("I have no data for the exchange rate for future!")


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

excahge_rate_library()



