# Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
#    На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
#    Кількість символів в блоках - та, яка введена в другому параметрі.
#    Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
#    В репозиторій додайте і ті файли, по яким робили тести.
#    Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл, а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість. 
# В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
#    Наприклад:

#    █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
#                     ⏫ центр

#    █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
#                     ⏫ центр


def characters_set(file, characters_number):

	f = open(file, "r")
	result = f.read()
	print(len(result))
	f.close()

	if len(result) <=2  and characters_number < 2 :
		start = result[0:characters_number]
		middle ="Sorry I don`t know what to print here"
		end = result[-characters_number:]
		print(start, "*****", middle, "*****", end )

	elif len(result)<characters_number:
		print("Sorry, characters_number should not be greater then characters in file" )

	elif len(result) % 2 == 0 and characters_number % 2 == 0:
		start = result[0:characters_number]
		middle = result[int((len(result)/2)-(characters_number//2)):int((len(result)/2)+(characters_number//2))]
		end = result[-characters_number:]
		print(start, "*****", middle, "*****", end )

	elif len(result) % 2 == 0 and characters_number % 2 > 0:
		start = result[0:characters_number]
		middle = result[int((len(result)/2)-((characters_number//2)+1)):int((len(result)/2)+(characters_number//2))]
		end = result[-characters_number:]
		print(start,"*****",middle,"*****", end)

	elif len(result) % 2 > 0 and characters_number % 2 == 0:
		start = result[0:characters_number]
		middle = result[int(((len(result)/2)+1)-(characters_number//2)):int(((len(result)/2)+1)+(characters_number//2))]
		end = result[-characters_number:]
		print(start,"*****",middle,"*****", end)

	elif len(result) % 2 > 0 and characters_number % 2 > 0:
		start = result[0:characters_number]
		middle = result[int(((len(result)/2)+1)-((characters_number//2)+1)):int(((len(result)/2)+1)+(characters_number//2))]
		end = result[-characters_number:]
		print(start,"*****",middle,"*****", end)

# characters_set("test2.txt", 1)
# characters_set("test1.txt", 1)
# characters_set("test.txt", 1)