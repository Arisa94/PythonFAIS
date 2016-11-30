from points import *

class Rectangle:

	def __init__(self, x1=0, y1=0, x2=0, y2=0):
		if(x1 > x2):
			raise ValueError("x1 cannot be bigger than x2!")
		if(y1 > y2):
			raise ValueError("y1 cannot be bigger than y2!")
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	def __str__(self):
		return str("[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]")

	def __repr__(self):
		return str("Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", "+ str(self.pt2.y) + ")")

	def __eq__(self, other):
		return (self.pt1== other.pt1 and self.pt2 == other.pt2)

	def __ne__(self, other):
		return not self == other

	def center(self):
		return Point((self.pt2.x + self.pt1.x) / 2, (self.pt2.y + self.pt1.y) / 2)

	def area(self):
		return(self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

	def move(self, x, y):
		self.pt1.x = self.pt1.x + x
		self.pt2.x = self.pt2.x + x
		self.pt1.y = self.pt1.y + y
		self.pt2.y = self.pt2.y + y

	def intersection(self, other):
		return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

	def cover(self, other):
		return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

	def make4(self):     # zwraca list czterech mniejszych
		middleX = (self.pt2.x - self.pt1.x) / 2
		middleY = (self.pt2.y - self.pt1.y) / 2
		return [Rectangle(self.pt1.x, self.pt1.y, middleX, middleY), Rectangle(middleX,  self.pt1.y, self.pt2.x, middleY), Rectangle(self.pt1.x, middleY, middleX, self.pt2.y), Rectangle(middleX, middleY, self.pt2.x, self.pt2.y)]

