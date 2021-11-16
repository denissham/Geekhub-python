#Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#		Sample data : 1, 5, 7, 23
#		Output :
#		List : [‘1', ' 5', ' 7', ' 23']
#		Tuple : (‘1', ' 5', ' 7', ' 23')


my_input = input('Please input comma separated numbers: ')
my_list = my_input.split(',')
my_tuple = tuple(my_list)

print('Your input was: ' + my_input)
print('List:', my_list)
print('Tuple:', my_tuple)
