# На основі попередньої функції створити наступний кусок кода:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)

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
   
   if len(password) <= 8 and a == 0:
      raise MyErrorPassword("Пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру")

   if username == password:
      raise MyErrorThird("Ім'я та пароль не повинні співпадати")

   print(username)
   print(password)
   print("Status: OK")
   
users_list = []

for i in range(5):
   user=[]
   username = str(input("Введіть username: "))
   password = str(input("Введіть password: "))
   user.extend([username, password])
   users_list.append(user)

def user_validation(users_list):
   for i in users_list:
      username = i[0]
      password = i[1]
      try:
         validation(username, password)
         
         
      except MyErrorUsername as e:
         print(username)
         print(password)
         print("Status:", e) 
      except MyErrorPassword as er:
         print(username)
         print(password)
         print("Status:", er)
      except MyErrorThird as erro:
         print(username)
         print(password)
         print("Status:", erro)
      

user_validation(users_list)
 



