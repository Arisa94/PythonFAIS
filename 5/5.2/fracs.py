from fractions import gcd

def add_frac(frac1, frac2):        # frac1 + frac2
    result = [0, 0]
    result[0] = (frac1[0] * frac2[1]) + (frac2[0] * frac1[1])
    result[1] = frac1[1] * frac2[1]
    temp = gcd(result[0], result[1])
    result[0] = result[0] / temp
    result[1] = result[1] / temp
    return result
 
def sub_frac(frac1, frac2):       # frac1 - frac2
    result = [0, 0]
    result[0] = (frac1[0] * frac2[1]) - (frac2[0] * frac1[1])
    result[1] = frac1[1] * frac2[1]
    temp = gcd(result[0], result[1])
    result[0] = result[0] / temp
    result[1] = result[1] / temp
    return result
 
 
def mul_frac(frac1, frac2):        # frac1 * frac2
    result = [0, 0]
    result[0] = frac1[0] * frac2[0]
    result[1] = frac1[1] * frac2[1]
    temp = gcd(result[0], result[1])
    result[0] = result[0] / temp
    result[1] = result[1] / temp
    return result
   
def div_frac(frac1, frac2):         # frac1 / frac2
    result = [0, 0]
    result[0] = frac1[0] * frac2[1]
    result[1] = frac1[1] * frac2[0]
    temp = gcd(result[0], result[1])
    result[0] = result[0] / temp
    result[1] = result[1] / temp
    return result
 
def is_positive(frac):             # bool, czy dodatni
    return((frac[0] * frac[1]) > 0)
 
def is_zero(frac):                 # bool, typu [0, x]
    return (frac[0] == 0)
 
def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    temp1 = frac1[0] * frac2[1]
    temp2 = frac2[0] * frac1[1]
    if temp1 == temp2:
        return 0
    if temp1 > temp2:
        return 1
    else:
        return -1
   
def frac2float(frac):             # konwersja do float
    return float(float(frac[0]) / float(frac[1]))
 
f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznacznosc)
f5 = [0, 2]                   # zero (niejednoznacznosc)
 
import unittest
 
class TestFractions(unittest.TestCase):

	def setUp(self):
		self.zero = [0, 1]

	def test_add_frac(self):
		self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

	def test_sub_frac(self):
		self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
	   
	def test_mul_frac(self):
		self.assertEqual(mul_frac([4, 3], [15, 7]), [20, 7])

	def test_div_frac(self):
		self.assertEqual(div_frac([1, 2], [1, 6]), [3, 1])

	def test_is_positive(self):
		self.assertEqual(is_positive([-1, 2]), False)
		self.assertEqual(is_positive([1, 2]), True)
		self.assertEqual(is_positive([-1, -2]), True)
	   
	def test_is_zero(self):
		self.assertEqual(is_zero([0, 2]), True)
		self.assertEqual(is_zero([1, 2]), False)

	def test_cmp_frac(self):
		self.assertEqual(cmp_frac([1, 2], [1, 6]), 1)
		self.assertEqual(cmp_frac([1, 2], [3, 6]), 0)
		self.assertEqual(cmp_frac([1, 2], [10, 6]), -1)
	   
	def test_frac2float(self):
		self.assertEqual(frac2float([1, 2]), 0.5)

	def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy