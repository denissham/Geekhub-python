# Користувачем вводиться початковий і кінцевий рік. 
# Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

start_year = int(input('Please input start year: '))
end_year = int(input('Please input end year: '))

for i in range(start_year, end_year +1):
	if i % 100 != 0:
		if i % 4 == 0:
			print(i)
	elif i % 400 == 0:
		print(i)	