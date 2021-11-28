# Написати функцию < is_prime >,
# яка прийматиме 1 аргумент - число від 0 до 1000, 
# і яка вертатиме True, якщо це число просте, и False - якщо ні.

def is_prime(number = int(input("Введіть число від 0 до 1000: "))):
	
	if number == 2 or number == 3:
		print(True)
	elif number == 0 or number == 1:
		print("Це не визначене число")
	elif 3 < number <= 1000:
		a = 0

		for i in range(2, number):
			result = number/i
			decimal = result - int(result)
			
			if decimal == 0:
				a = a + 1
		if a > 0:
			print(False)
		else:
			print(True)
	elif number > 1000:
		print("Вибачте але я приймаю числа до 1000")

is_prime()



