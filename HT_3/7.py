# Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator(a,b,operation):
	if operation == "*":
		result = a * b
	elif operation == "+":
		result = a + b
	elif operation == "-":
		result = a - b
	elif operation == "/":
		result = a/b
	print(result)

a = int(input("Введіть перше число: "))
operation = input("Введіть знак операції: ")
b = int(input("Введіть друге число: "))

calculator(a,b,operation)