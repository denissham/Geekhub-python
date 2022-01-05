# 2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні. 
# Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   # - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.

class Person(object):

	def __init__(self, age : int, name:str):
		self.__age = age
		self.__name = name

	def show_age(self):
		return self.__age

	def print_name(self):
		return self.__name

	def show_all_information(self):
		return f"{self.__name}-{self.__age}"

user1 = Person(19, "John")
print(user1.show_age())
print(user1.print_name())
print(user1.show_all_information())
user1.profession = "Teacher"
print(user1.profession)

user2 = Person(25, "Ryan")
print(user2.show_age())
print(user2.print_name())
print(user2.show_all_information())
user2.profession = "Engineer"
print(user2.profession)