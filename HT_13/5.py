# Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).

class Library(object):
	def __init__(self):
		self.books_list = []

	def addItem(self,book):
		self.books_list.append(book)

	def show_books(self):
		for book in self.books_list:
			print(book.__dict__)

	def remove_book(self):
		book_to_remove = input("Введіть назву книги яку хочете взяти: ")
		for book in self.books_list:
			if book.__dict__["title"] == book_to_remove:
				self.books_list.remove(book)
		

	def book_search_title(self):
		title_input = input("Введіть назву книги: ")
		count = []
		for book in self.books_list:
			if book.__dict__["title"] == title_input:
				print(f"Ось книга яку ви шукали: -> {book.__dict__}")
			else:
				count.append("false")
		if len(count) == len(self.books_list):
			print("Данної книги немає в нашій бібліотеці. Тихо повинно бути в бібліотеці!")

	def book_search_author(self):
		author_input = input("Введіть автора книги: ")
		count = []
		for book in self.books_list:
			if book.__dict__["author"] == author_input:
				print(f"Ось книга яку ви шукали: -> {book.__dict__}")
			else:
				count.append("false")
		if len(count) == len(self.books_list):
			print("Данної книги немає в нашій бібліотеці. Тихо повинно бути в бібліотеці!")

class Book(object):
	def __init__(self,title,description,author):
		self.title = title
		self.description = description
		self.author = author
    

def school_library():

	myLibrary = Library()
	book1 = Book("ЯДС","Я Досліджую Світ","Іщенко")
	book2 = Book("Математика ч1","Математика 1 частина","Скворцова")
	book3 = Book("Математика ч2","Математика 2 частина","Онопрієнко")
	book4 = Book("Трудівничок","Труди для дітей 1го класу","Савченко")
	myLibrary.addItem(book1)
	myLibrary.addItem(book2)
	myLibrary.addItem(book3)
	myLibrary.addItem(book4)
	menu(myLibrary)

def menu(myLibrary):
	action = int(input("""Введіть дію яку ви хочете виконати:
	1. Взяти книгу
	2. Знайти книгу
	3. Додати книгу
	4. Показати книги наявні в бібліотеці 
		"""))
	if action == 1:
		myLibrary.remove_book()
		continue_action = input("Хочете продовжити y/n: ")
		if continue_action == "y":
			menu(myLibrary)
		else:
			exit()

	if action == 2:
		action_search = int(input("""Введіть як саме ви хочете знайти книгу:
	1. По назві
	2. По автору
		"""))
		if action_search == 1:
			myLibrary.book_search_title()
			continue_action = input("Хочете продовжити y/n: ")
			if continue_action == "y":
				menu(myLibrary)
			else:
				exit()
		elif action_search == 2:
			myLibrary.book_search_author()
			continue_action = input("Хочете продовжити y/n: ")
			if continue_action == "y":
				menu(myLibrary)
			else:
				exit()
		else:
			print("Вибраного пункту не існує")
			menu(myLibrary)
		
	if action == 3:
		title = input("Введіть назву книги")
		description = input("Введіть опис книги")
		author = input("Введіть автора книги")
		book_to_add = Book(title, description, author)
		myLibrary.addItem(book_to_add)
		continue_action = input("Хочете продовжити y/n: ")
		if continue_action == "y":
			menu(myLibrary)
		else:
			exit()

	if action == 4:
		myLibrary.show_books()
		continue_action = input("Хочете продовжити y/n: ")
		if continue_action == "y":
			menu(myLibrary)
		else:
			exit()


school_library()

