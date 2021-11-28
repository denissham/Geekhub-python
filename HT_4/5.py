# Написати функцію < fibonacci >, 
# яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(number = int(input("Введіть число: "))):
	if number < 0:
		print("Будь ласка введіть число більше 0")
	elif number == 0:
		my_list = []
		my_list.append(number)
		print("Вашe число Фібоначчі =", my_list)
	elif number == 1:
		my_list = []
		my_list.extend([0, 1])
		print("Ваші числа Фібоначчі =",  my_list) 
	elif number > 1:
		my_list = [0, 1]
		current = 1
		for index, elem in enumerate(my_list):
			if elem < number:
				while current < number:
					previous = int(my_list[index-1])
					pre_previous = int(my_list[index-2])
					current = previous + pre_previous
					if current > number:
						break
					else:
						my_list.append(current)

		print("Ваші числа Фібоначчі =", my_list)

fibonacci()