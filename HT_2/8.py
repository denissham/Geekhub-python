 # Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа,
 #   а значення для цих ключів - це квадрат ключа.
	# 	Приклад виводу при введеному значенні 5 :
	# 	{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

my_input = int(input('Please input number: '))

my_dict = {}
for i in range(my_input + 1):
	my_key = i
	my_value = my_key**2
	my_dict.update({my_key: my_value})

print(my_dict)