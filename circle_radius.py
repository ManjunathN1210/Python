"""

Question:
	Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
	
	Hints:
	
	Use def methodName(self) to define a method.

"""

class Circle:
	
	def __init__(self,r):
		
		self.r = r
	
	def area(self):
		
		return 3.14*(self.r**2)

circle = Circle(5)
print(circle.area())
