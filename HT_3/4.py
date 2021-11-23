# Створiть 3 рiзних функцiї (на ваш вибiр). 
# Кожна з цих функцiй повинна повертати якийсь результат. 
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. 
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def function_1(x = 2):
	return x

def function_2(y = "TEST"):
	return y


def function_3(z = 6):
	return z


def function_4():
	w = str(function_1()) + str(function_2()) + str(function_3())
	print(w)
	return



function_4()

