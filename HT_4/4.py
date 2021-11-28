 # Написати функцію < prime_list >, 
 # яка прийматиме 2 аргументи - початок і кінець діапазона, 
 # і вертатиме список простих чисел всередині цього діапазона.

def prime_list(number_1 = int(input("Введіть перше число: ")), number_2 = int(input("Введіть друге число: "))):
	list_prime = []

	for j in range(number_1, number_2 + 1):
		
		if j == 2 or j == 3:
			list_prime.append(j)

		elif j > 3:
			a = 0

			for i in range(2, j):
				result = j/i
				decimal = result - int(result)

				if decimal == 0:
					a = a + 1

			if a == 0:
				list_prime.append(j)

	print(list_prime)

prime_list()