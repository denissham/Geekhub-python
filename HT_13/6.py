# Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class Counter(object):
	instance_count = 0
	
	def instance_counter(self):
		Counter.instance_count += 1
		return Counter.instance_count
		

instance1 = Counter()
print(instance1.instance_counter())
instance2 = Counter()
print(instance2.instance_counter())
instance3 = Counter()
print(instance3.instance_counter())
instance4 = Counter()
print(instance4.instance_counter())