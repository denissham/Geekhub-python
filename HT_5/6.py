# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range

def func(start=0,stop=0,step=1):
	start = int(start)
	stop = int(stop)
	result = start
	if step > 0:
		while result < stop:
			yield result
			result += step

	elif step < 0 and stop < 0:
		while result > stop:
			yield result
			result += step

	elif step <= 0 and stop >= 0:
		return False

f = func(2,-10, -2)

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


