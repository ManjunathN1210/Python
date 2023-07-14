"""

Write a function to compute 5/0 and use try/except to catch the exception.

Hints:
	Use try/except to catch exception.

"""

def divide(num1, num2):
	return num1/num2
	
num1 = 5
num2 = 0


try:
	print(divide(num1,num2))
except ZeroDivisionError:
	print("Divide by zero error")
except Exception as err:
	print("Exception "+str(err))
finally:
	print("Finally block")

