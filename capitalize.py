"""

Write a program that accepts sequence of lines as input and prints the line after making all the characters in the sentence capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Output :- 
HELLO WORLD
PRACTICE MAKES PERFECT

"""

lines = []
while True:
	s = input()
	if s:
		lines.append(s)
	else:
		break

for sentence in lines:
	print(sentence.upper())
