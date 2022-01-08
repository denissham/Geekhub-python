# Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class Counter(object):
	instance_count = 0
	
	def __init__(self):
		Counter.instance_count += 1
		

instance1 = Counter()
print(instance1.instance_count)
instance2 = Counter()
print(instance2.instance_count)
instance3 = Counter()
print(instance3.instance_count)
instance4 = Counter()
print(instance4.instance_count)