# Write a script to check whether a specified value is contained in a group of values
# Test Data :
		# 3 -> [1, 5, 8, 3] : True
		# -1 -> (1, 5, 8, 3) : False

my_input = input('Please input comma separated numbers as a test data: ')
test_list = my_input.split(',')
my_element = input('Please input element which should be found in a test data: ')
if my_element in test_list:
	print(my_element, '->', test_list, ':', True)
else:
	print(my_element, '->', test_list, ':', False)
