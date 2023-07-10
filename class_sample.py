"""

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""

class InputOutputString:
	
	def __init__(self):
		self.s = ""
		print("Enter some string")
	
	def getString(self):
		self.s = input()
	
	def printString(self):
		print("The Entered String in uppercase",self.s.upper())
	
	def testDef(self):
		print("This is a test method")
		
instance = InputOutputString()
instance.getString()
instance.printString()
instance.testDef()
