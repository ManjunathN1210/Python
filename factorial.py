"""

Question:

Write a program which can compute the factorial of a given number.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:

8
Then the output should be 40320

"""

def factorial(num):
	if num == 0:
		return 1
	return (num*factorial(num-1))

num = int(input("Enter a number: \n"))
print(factorial(num))
