 #
# multiply_numbers.py
#
# Created by: Sbastian N
# Created on: April 9
#
# This program lets the user add numbers

# Function
def multiply_numbers():
	# This variables would be the global declaration of the outside variables in the function 
	# global the_addition
	# global multiple_one_input
	# global multiple_one
	# global multiple_two_input
	# global multiple_two

	# This variables would be declared inside the function to avoid the global declaration 
	the_addition = 0
	multiple_one_input = input('What is the first multiple: ')
	multiple_one = int(multiple_one_input)
	multiple_two_input = input('What is the second multiple: ')
	multiple_two = int(multiple_two_input)

	# Function of the addition 
	if multiple_two > 0:
		while (multiple_two is not 0):
			the_addition = the_addition + multiple_one
			multiple_two = multiple_two - 1
		print 'This is the result: ', str(the_addition)
	elif multiple_two < 0:
		while (multiple_two is not 0):
			the_addition = the_addition + (-multiple_one)
			multiple_two = multiple_two + 1
		print 'This is the result: ', str(the_addition)
	elif multiple_two == 0:
		print 'This is the result: ', str(the_addition)


# This set of variables would have to be used combined with the global declaration of the variables inside the function
# the_addition = 0
# multiple_one_input = input('What is the first multiple: ')
# multiple_one = int(multiple_one_input)
# multiple_two_input = input('What is the second multiple: ')
# multiple_two = int(multiple_two_input)

# Calling the function
the_result = multiply_numbers()
input()