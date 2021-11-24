# Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!


def calculator():
	while True:
		try:
			a = int(input("Введіть перше число: "))
			operation = input("Введіть знак операції: ")
			b = int(input("Введіть друге число: "))
		except ValueError:
			print("Ви ввели щось не зрозуміле")
			continue
		except KeyboardInterrupt:
			print("Ви ввели щось не зрозуміле")
			continue
		else:
			break

	if operation == "*":
			result = a * b
			print(result)
	elif operation == "+":
			result = a + b
			print(result)
	elif operation == "-":
			result = a - b
			print(result)
	elif operation == "/":
		if 0 < b > 0:
			result = a/b
			print(result)
		else:
			print("Вибачайте, але на 0 не можна ділити")
	else:
			print("Соррян, я не настільки крутий, щоб порахувати те, що ви ввели!")
	
calculator()