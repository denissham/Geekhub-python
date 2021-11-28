# Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць 
# строком на < years > років під < percents > відсотків 
# (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу 
# і в наступному році на них також нараховуються відсотки). 
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). 
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.

def bank(value, years, percents = 10):
	
	for i in range(1, years+1):
		years_percents = round(value * (percents/100), 2)
		value = value + years_percents
	
	print(value)
	return

value = int(input("Введіть сумму вкдаду: "))
years = int(input("Введіть кількість років: "))
percents = input("Введіть під який відсоток: ")
if not percents:
	bank(value, years)
else:
	percents = int(percents)
	bank(value, years, percents)