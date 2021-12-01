# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#    Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#    Логіка наступна:
#        якщо введено коректну пару ім'я/пароль - вертається <True>;
#        якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
class LoginException(Exception):
	pass


def user_auth(username, password, silent = False):
	users = [{"denys":"123456"}, {"Test":"654321"}, {"admin":"admin"}, {"user":"user"}, {"testtest":"qwerty"}]

	for i in users:
		a = bool
		for key,value in i.items():
			if key == username and value == password:
				a = True
			else:
				a = False
		if a == True:
			break

	if a == True:
		print(True)
		
	elif a == False and silent == True:
		print(False)
	elif a == False and silent == False:
		raise LoginException("Ви ввели не правельны данні")
				
username = str(input("Введіть username: "))
password = str(input("Введіть password: "))
silent = input("Введіть silent(Необов'язково): ")
if not silent:
	user_auth(username, password)
else:
	silent = bool(silent)
	user_auth(username, password, silent)
