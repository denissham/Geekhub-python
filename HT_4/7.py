# Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

def same_elements(elements = input("Введіть елементи розділені комою: ")):
	my_list = elements.split(',')
	result = {}
	for i in my_list:
		if i not in result:
			result[i] = 1
		else:
			result[i] = result[i] + 1
	print("Результат: ", )
	for key,value in result.items():
		print(key, "-", value, "раз(а)")

same_elements()