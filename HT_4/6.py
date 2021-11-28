# Вводиться число. 
# Якщо це число додатне, знайти його квадрат, 
# якщо від'ємне, збільшити його на 100, 
# якщо дорівнює 0, не змінювати.

def change_number(number = int(input("Введіть число: "))):
	result = int()
	if number > 0:
		result = number**2
		print("Квадрат числа =", result)
	elif number < 0:
		result = number + 100
		print("Число + 100 =", result )
	else:
		print("Ваше число =",  number ) 
	
change_number()