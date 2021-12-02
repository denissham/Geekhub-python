# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range

def func(*args):

	my_args = list(args)
	if len(args) == 1:
		start = 0
		stop = int(args[0])
		step = 1
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
		
	elif len(args) == 2:
		start = int(args[0])
		stop = int(args[1])
		step = 1
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
		
		
	elif len(args) >= 3:
		start = int(args[0])
		stop = int(args[1])
		step = int(args[2])
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

f = func(10)

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


