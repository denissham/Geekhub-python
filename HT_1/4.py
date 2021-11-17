# Write a script to concatenate N strings.

n = int(input('Please input strings quantity: '))
my_strings = [str(input('Enter a string: ')) for i in range(n)]
summ = "".join(my_strings)
print(summ)