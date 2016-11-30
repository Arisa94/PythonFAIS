from rectangles import *
from points import Point
import unittest

class TestRectangle(unittest.TestCase):

	def setUp(self):
		self.first = Rectangle(1, 2, 3, 4)
		self.second = Rectangle(2, 2, 4, 5)

	def test_init(self):
		with self.assertRaises(ValueError):
			Rectangle(5, 1, 2, 3)
		self.assertEqual(self.first.pt1, Point(1, 2))
		self.assertEqual(self.first.pt2, Point(3, 4))
		self.assertEqual(self.second.pt1.x, 2)		

	def test_str(self):
		self.assertEqual(str(self.first), "[(1, 2), (3, 4)]")

	def test_repr(self):
		self.assertEqual(repr(self.first), "Rectangle(1, 2, 3, 4)")
		
	def test_eq(self):
		self.assertTrue(self.first == Rectangle(1,2,3,4))
		self.assertFalse(self.first == self.second)
	
	def test_ne(self):
		self.assertFalse(self.first != Rectangle(1,2,3,4))
		self.assertTrue(self.first != self.second)
	
	def test_center(self):
		self.assertEqual(self.first.center(), Point(2, 3))
	
	def test_area(self):
		self.assertEqual(self.first.area(), 4)
	
	def test_move(self):
		self.first.move(1, 2)
		self.assertEqual(self.first.pt1.x, 2)
		self.assertEqual(self.first.pt2.y, 6)
	
	def test_intersection(self):
		self.assertEqual(self.first.intersection(self.second), Rectangle(2, 2, 3, 4))
	
	def test_cover(self):
		self.assertEqual(self.first.cover(self.second), Rectangle(1, 2, 4, 5))
	
if __name__ == '__main__':
	unittest.main()