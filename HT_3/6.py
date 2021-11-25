# Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя

def string_calculation(my_string):
	if 30 < len(my_string) < 50:
		print("Довжина рядка: ", len(my_string))
		characters_count = 0
		numbers_count = 0
		for i in my_string:
			if i.isnumeric():
				numbers_count +=1
			elif i.isalpha():
				characters_count += 1

		print("Kiлькiсть букв: ", characters_count)
		print("Kiлькiсть цифр: ", numbers_count)

	elif len(my_string) <= 30:
		characters_sum = ""
		numbers_sum = 0
		for j in my_string:
			if j.isnumeric():
				numbers_sum = numbers_sum + int(j)
			elif j.isalpha():
				characters_sum = "".join((characters_sum, j))
		print("Сума всіх чисел:", numbers_sum)
		print("Рядок без цифр:", characters_sum)

	elif len(my_string) >= 50:
		revers_characters = ''.join(reversed(my_string))
		print("Перевернутий рядок: ", revers_characters)

my_string = str(input("Введіть деякий рядок букв та цифр: "))   

string_calculation(my_string)