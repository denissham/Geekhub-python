# Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), 
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def season(month):
	if month in [12,1,2]:
		return "Зима"
	elif month in [3,4,5]:
		return "Весна"
	elif month in [6,7,8]:
		return "Літо"
	elif month in [9,10,11]:
		return "Осінь"
	else:
		return "Вибачайте, але таких місяців немає!"

result = season (int(input("Введіть № місяця: ")))
print(result)
	
