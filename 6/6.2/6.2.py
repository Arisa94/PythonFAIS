from points import *
import unittest

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_init(self):
    	tmp = Point(2, 3)
    	self.assertIsInstance(tmp, Point)
    	self.assertIs(tmp.x, 2)
    	self.assertIs(tmp.y, 3)

    def test_str(self):
    	tmp = Point(5, 6)
    	self.assertIsInstance(str(tmp), str)
    	self.assertEqual(str(tmp), "(5, 6)")

    def test_repr(self):
    	tmp = Point(7, 9)
    	self.assertIsInstance(repr(tmp), str)
    	self.assertEqual(repr(tmp), "Point(7, 9)")

    def test_eq(self):
    	tmp = Point(5, 7)
    	self.assertTrue(tmp == Point(5, 7))
    	self.assertFalse(tmp == Point(5, 5))
    	self.assertFalse(tmp == Point(0, 0))

    def test_ne(self):
    	tmp = Point(3, 3)
    	self.assertTrue(tmp != Point(1, 7))
    	self.assertTrue(tmp != Point(0, 0))
    	self.assertFalse(tmp != Point(3, 3))

    def test_add(self):
    	tmp = Point(3, 2)
    	self.assertEqual(tmp + tmp, Point(6, 4))
    	self.assertEqual(tmp + Point(5, 7), Point(8, 9))
    	self.assertEqual(tmp + Point(0, 0), tmp)
    
    def test_sub(self):
    	tmp = Point(5, 4)
    	self.assertEqual(tmp - tmp, Point(0, 0))
    	self.assertEqual(tmp - Point(5, -2), Point(0, 6))
    	self.assertEqual(tmp - Point(0, 0), tmp)

    def test_mul(self):
    	tmp = Point(5, 5)
    	self.assertEqual(tmp * Point(3, 4), 35)
    	self.assertEqual(tmp * Point(0, 0), 0)
    	self.assertEqual(tmp * tmp, 50)

    def test_cross(self):
    	tmp = Point(4,5)
    	self.assertEqual(tmp.cross(tmp), 0)
    	self.assertEqual(tmp.cross(Point(0, 0)), 0)
    	self.assertEqual(tmp.cross(Point(3, 4)), 1)

    def test_length(self):
    	self.assertEqual(Point(9, 0).length(), 9)
    	self.assertEqual(Point(4, 3).length(), 5)
    	self.assertEqual(Point(0, 0).length(), 0)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
