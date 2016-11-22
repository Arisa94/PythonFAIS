from fracs import *
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self): pass

    def test_cmp(self):
    	self.assertEqual(cmp(Frac(1, 2), Frac(1, 2)), 0)
    	self.assertEqual(cmp(Frac(1, 2), Frac(2, 2)), -1)
    	self.assertEqual(cmp(Frac(1, 2), Frac(0, 1)), 1)

    def test_pos(self):
    	self.assertEqual(+Frac(1, 2), Frac(1, 2))
    	self.assertEqual(+Frac(-1,  2), Frac(-1,  2))
    	self.assertEqual(Frac(0, 1), Frac(0, 1))

    def test_neg(self):
    	self.assertEqual(-Frac(1, 2), Frac(-1,  2))
    	self.assertEqual(-Frac(-1,  2), Frac(1, 2))
    	self.assertEqual(-Frac(0, 1), Frac(0, 1))
    	self.assertEqual(-(-Frac(1, 2)), Frac(1, 2))

    def test_invert(self):
    	self.assertEqual(~Frac(1, 2), Frac(2, 1))
    	self.assertEqual(-(~Frac(-1,  2)), Frac(2, 1))

    def test_float(self):
        self.assertIsInstance(float(Frac(1, 2)), float)
        self.assertIsInstance(float(Frac(0, 1)), float)

    def test_repr(self):
        self.assertIsInstance(repr(Frac(1, 2)), str)
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")

    def test_str(self):
        self.assertIsInstance(str(Frac(1, 2)), str)

    def test_init(self):
        self.assertEqual(Frac(1, 2).x, 1)
        self.assertEqual(Frac(1, 2).y, 2)

    def test_add_frac(self):
    	
    	self.assertEqual(Frac(1, 2) + Frac(1, 2), Frac(2, 2))
    	self.assertEqual(Frac(1, 2) + (-Frac(1, 2)), Frac(0, 1))
    	self.assertEqual(Frac(2, 2) + (-Frac(1, 2)), Frac(1, 2))

    def test_sub(self):
        self.assertEqual(Frac(1, 2)-Frac(1,2), Frac(0, 1))
        self.assertEqual(Frac(1, 2) - (-Frac(1, 2)), Frac(2, 2))
        self.assertEqual(Frac(2, 2) + (-Frac(1, 2)), Frac(1, 2))

    def test_mul(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 2), Frac(1, 1))
        self.assertEqual(Frac(1, 2) / -Frac(1, 2), Frac(-1, 1))

    def test_div(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 2), Frac(1, 4))
        self.assertEqual(Frac(1, 2) * -Frac(1, 2), Frac(-1, 4))
        self.assertEqual(Frac(1, 2) * Frac(0, 1), Frac(0, 1))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
