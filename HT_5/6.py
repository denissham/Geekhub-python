# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range

def func(*args):

	my_args = list(args)
	if len(args) == 1:
		start = 0
		stop = int(args[0])
		step = 1
			
		if stop <= 0:
			return False

		else:
			while result < stop:
				yield result
				result += step
			
		
	elif len(args) == 2:
		start = int(args[0])
		stop = int(args[1])
		step = 1

		if stop <=0 and start <=0 and start>stop:
			return False
			
		else:
			result = start
			while result < stop:
				yield result
				result += step	
		
	elif len(args) >= 3:
		start = int(args[0])
		stop = int(args[1])
		step = int(args[2])
		if step > 0:
			result = start
			while result < stop:
				yield result
				result += step

		elif step < 0 and stop < 0:
			result = start
			while result > stop:
				yield result
				result += step

		elif step < 0 and stop > 0 and stop < start:
			result = start
			while result > stop:
				yield result
				result += step

		elif step <= 0 and stop >= 0 and stop > start:
			return False



f = func(30,20,-1)

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

