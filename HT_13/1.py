# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, 
# а саме додавання, віднімання, множення, ділення.
#    - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
#    - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
#    - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )

class Calc(object):
	""" Class with last_result attributes + 
	4 methods which are doing simple math operations"""

	last_result = None

	def addition(self, x:float, y:float) -> float:
		self.last_result = x + y
		return self.last_result

	def subtraction(self, x:float, y:float) -> float:
		self.last_result = x - y
		return self.last_result

	def multiplication(self, x:float, y:float) -> float:
		self.last_result = x * y
		return self.last_result

	def division(self, x:float, y:float)-> float:
		if y == 0:
			self.last_result = "Error Division by 0"
			return self.last_result
		else:
			self.last_result = x / y
			return self.last_result

a = Calc()

print(a.last_result)
a.addition(6, 7)
print(a.last_result)
a.division(9, 3)
print(a.last_result)
a.subtraction(13, 7)
print(a.last_result)
a.multiplication(13, 7)
print(a.last_result)
