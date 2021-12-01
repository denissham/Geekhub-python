# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#    - щось своє :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

class MyErrorUsername(Exception):
	pass

class MyErrorPassword(Exception):
	pass

class MyErrorThird(Exception):
	pass

def validation(username, password):
	a = 0
	for i in password:
		if i.isnumeric():
			a += 1

	if len(username) < 3 or len(username) > 50:
		raise MyErrorUsername("Ім'я повинно бути не меншим за 3 символа і не більшим за 50")
			return(MyErrorUsername)
	
	if len(password) <= 8 and a == 0:
		raise MyErrorPassword("Пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру")

	if username == password:
		raise MyErrorThird("Ім'я та пароль не повинні співпадати")

	return True
	

username = str(input("Введіть username: "))
password = str(input("Введіть password: "))

validation(username, password)