# Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
		# Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
		# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

sample_data = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
new_list = []
for i in sample_data:
	if len(i) != 0:
		new_list.append(i)
		
print(new_list)
