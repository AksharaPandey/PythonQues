
def reverse(number):
number = input(int("Enter the number:"))
rev_number = 0
while (number > 0):
	remainder = number % 10
	rev_number = (rev_number * 10) + remainder
	number //= 10
