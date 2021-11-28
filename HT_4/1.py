 # Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, 
	# і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.

def square(side_a):
	square_area = side_a**2
	perimeter_square = side_a*4
	diagonal_square = round((2**(0.5))*side_a, 2)
	result_list = []
	result_list.extend([square_area, perimeter_square, diagonal_square])
	result_tuple = tuple(result_list)
	print("Площа квадрата, Периметр квадрата, Діагональ квадрата: ", result_tuple)
	return

side_a = int(input("Введіть сторону квадрата: "))
square(side_a)