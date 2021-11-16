# Write a script to concatenate N strings.

my_strings = input('Please input comma separated strings: ')

my_list = my_strings.split(',')
summ = "".join(my_list)
print(summ)