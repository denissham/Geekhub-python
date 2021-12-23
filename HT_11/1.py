# Сайт для виконання завдання: https://jsonplaceholder.typicode.com
# Написати програму, яка буде робити наступне:
# 1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
# 2. Запропонувати обрати користувача (ввести ID)
# 3. Розробити наступну менюшку (із вкладеними пунктами):
#    1. Повна інформація про користувача
#    2. Пости:
#       - перелік постів користувача (ID та заголовок)
#       - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
#    3. ТУДУшка:
#       - список невиконаних задач
#       - список виконаних задач
#    4. Вивести URL рандомної картинки
import json
import requests
import ast

def program():
	url = "https://jsonplaceholder.typicode.com/users"
	r = requests.get(url)
	response_value = r.text
	users = ast.literal_eval(response_value)
	for i in users:
		user_id = i['id']
		name = i['name']
		username = i['username']
		print(f"User id:  {user_id}")
		print(f"Name: {name};     Username: {username}")

	selected_user = int(input("Введіть будь ласка id юзера: "))
	menu(selected_user,users)
	
def menu(selected_user,users):
	print("""Введіть який пункт меню ви хочете вибрати:
           1. Повна інформація про користувача
           2. Пости
           3. TODO
           4. Картинка""")
	action = int(input())

	if action == 1:
		user_info(users, selected_user)
		action_return = input("Бажаєте продовжити роботу?(y/n): ")
		if action_return == "y":
			menu(selected_user,users)
		else:
			exit()

	if action == 2:
		posts(selected_user)
		action_return = input("Бажаєте продовжити роботу?(y/n): ")
		if action_return == "y":
			menu(selected_user,users)
		else:
			exit()

	if action == 3:
		todos(selected_user)
		action_return = input("Бажаєте продовжити роботу?(y/n): ")
		if action_return == "y":
			menu(selected_user,users)
		else:
			exit()

	if action == 4:
		image_url = "https://source.unsplash.com/random/300x200"
		r_image = requests.get(image_url, allow_redirects=False)
		response_value = r_image.text
		print("Ось шлях до вашої картинки:")
		print(r_image.headers['Location'])
		action_return = input("Бажаєте продовжити роботу?(y/n): ")
		if action_return == "y":
			menu(selected_user,users)
		else:
			exit()

def user_info(users, selected_user):
	for i in users:
		if i['id'] == selected_user:
			user_id = i['id']
			name = i['name']
			username = i['username']
			email = i['email']
			address = i['address']
			street = address['street']
			suite = address['suite']
			city = address['city']
			zipcode = address['zipcode']
			geo = address['geo']
			phone = i['phone']
			website = i['website']
			company = i['company']
			company_name = company['name']
			print(f"""Ось повна інформація про вибраного юзера:
Ім'я: {name}
Юзернейм: {username}
Email: {email}
Телефон: {phone}
Адреса: {street}, {suite}, {city}, {zipcode}, {geo}
Вебсайт: {website}
Компанія: {company_name}""")

def posts(selected_user):

	print("""Введіть що саме ви хочете зробити:
	       1. Подивитись всі пости користувача
	       2. Подивитись конкретний пост""")
	action_sub_menu = int(input())
	posts_url = f"https://jsonplaceholder.typicode.com/posts?userId={selected_user}"
	response = requests.get(posts_url)
	posts = json.loads(response.text)
	if action_sub_menu==1:
		print("Ось список постів вибраного Юзера: ")
		for post in posts:
			print(f"""ID поста: {post["id"]} 
Заголовок: {post["title"]}""")

	elif action_sub_menu == 2:
		print("Введіть ID поста який вам хочеться подивитись")
		action_post_id = int(input())
		for post in posts:
			if int(post["id"])==action_post_id:
				comments_url = f"https://jsonplaceholder.typicode.com/posts/{action_post_id}/comments"
				response = requests.get(comments_url)
				comments = json.loads(response.text)
				comments_ids = []
				for comment in comments:
					comments_ids.append(str(comment["id"]))

				print(f"""ID поста: {post["id"]} 
Заголовок: {post["title"]}
Текст Поста: {post["body"]}
Кількість коментарів: {len(comments_ids)} 
ID коментарів: {comments_ids}""")

def todos(selected_user):			
	print("""Введіть що саме ви хочете зробити:
	           1. Подивитись всі невиконані задачі користувача
	           2. Подивитись всі виконані задачі користувача""")
	action_todo = int(input())
	todo_url = f"https://jsonplaceholder.typicode.com/users/{selected_user}/todos"
	response = requests.get(todo_url)
	tasks_todo = json.loads(response.text)
	if action_todo == 1:
		print("Ось список невиконаних задач: ")
		for task in tasks_todo:
			if task["completed"] == False:
				print(task["title"])

	if action_todo == 2:
		print("Ось список виконаних задач: ")
		for task in tasks_todo:
			if task["completed"] == True:
				print(task["title"])

program()