"""

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them  alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied ot te question, it should be assumed to be a console input.

"""

input_str = input()
words = input_str.split(",") # Here we are trying to split the input string that is being passed
words.sort() # We sort the words alphabetically
print(",".join(words)) # Here we are trying to join the sorted words to make it as a sentence.
