# Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць 
# строком на < years > років під < percents > відсотків 
# (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу 
# і в наступному році на них також нараховуються відсотки). 
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). 
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.

def bank():
	value = bank_value()
	years = bank_years()
	percents = bank_percents()
	
	for i in range(1, years+1):
		years_percents = round(value * (percents/100), 2)
		value = value + years_percents
	
	print(value)
	return

def bank_value(value = int(input("Введіть сумму вкдаду: "))):
	return value

def bank_years(years = int(input("Введіть кількість років: "))):
	return years

def bank_percents():
	try:
		percents = int(input("Введіть кількість відсотків: "))
	except:
		percents = 10
	return percents

bank()