
# 1. Програма-світлофор.
#    Створити програму-емулятор світлофора для авто і пішоходів.
#    Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#    Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
#    Приблизний результат роботи наступний:
#       Red        Green
#       Red        Green
#       Red        Green
#       Red        Green
#       Yellow     Green
#       Yellow     Green
#       Green      Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Yellow     Red
#       Yellow     Red
#       Red        Green
#       .......

def generator(auto, pedestrian):
	while True:
		count = 0
		green_count = 0
		yellow_count = 0
		for i in auto:
		
			if i == "Red" and count <= 1:
				a = auto.index(i)
				b = pedestrian[a]
				count = count + 1
				yield '{0:10}  {1}'.format(i, b)
			
			elif i == "Red" and count == 2:
				a = auto.index(i)
				b = pedestrian[a + 2]
				count += 1
				yield '{0:10}  {1}'.format(i, b)	

			elif i == "Red" and count == 3:
				a = auto.index(i)
				b = pedestrian[a + 3]
				count = 0
				yield '{0:10}  {1}'.format(i, b)

			elif i == "Green" and green_count <= 1:
				a = auto.index(i)
				b = pedestrian[a]
				green_count += 1
				yield '{0:10}  {1}'.format(i, b)	

			elif i == "Green" and green_count == 2:
				a = auto.index(i)
				b = pedestrian[a+2]
				green_count = green_count + 1
				yield '{0:10}  {1}'.format(i, b)

			elif i == "Green" and green_count == 3:
				a = auto.index(i)
				b = pedestrian[a+3]
				green_count = 0
				yield '{0:10}  {1}'.format(i, b)

			elif i == "Yellow" and yellow_count <= 1:
				a = auto.index(i)
				b = pedestrian[a]
				yellow_count += 1
				yield '{0:10}  {1}'.format(i, b)

			elif i == "Yellow" and yellow_count == 2:
				a = auto.index(i)
				b = pedestrian[a+5]
				yellow_count += 1
				yield '{0:10}  {1}'.format(i, b)

			elif i == "Yellow" and yellow_count == 3:
				a = auto.index(i)
				b = pedestrian[a+6]
				yellow_count = 0
				yield '{0:10}  {1}'.format(i, b)


auto = ["Red","Red","Red","Red","Yellow","Yellow","Green","Green","Green","Green","Yellow","Yellow"]
pedestrian = ["Green","Green","Green","Green","Green","Green","Red","Red","Red","Red","Red","Red"]

f = generator(auto, pedestrian)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
