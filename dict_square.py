"""

Question:
	Define a function which can print a dictionary where the keys are numbers between 1 and 9 (both included) and the values are square of keys.
	
	Hints:
		Use dict[key]=value pattern to put entry into a dictionary.
		Use ** operator to get power of a number.
		

"""

def square():
	my_dict = {}
	for i in range(1,10):
		my_dict[i] = i**2
	
	print(my_dict)
	
	# This only prints the values
	
	for key,value in my_dict.items():
		print(value)

square()
