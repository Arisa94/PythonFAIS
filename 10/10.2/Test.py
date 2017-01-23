from Stack import *
import unittest


class Test(unittest.TestCase):

    def setUp(self):

        self.emptyStack = Stack(10)
        self.fullStack = Stack(1)
        self.fullStack.push(1)
        self.stack = Stack(10)

    def test_init(self):

        self.temp = Stack(5)
        self.assertEqual(self.temp.size, 5)
        self.assertEqual(self.temp.n, 0)

    def test_isEmpty(self):

        self.assertTrue(self.emptyStack.isEmpty())
        self.assertFalse(self.fullStack.isEmpty())

    def test_isFull(self):

        self.assertTrue(self.fullStack.isFull())
        self.assertFalse(self.emptyStack.isFull())

    def test_push(self):

        self.stack.push(5)
        self.assertEqual(1, self.stack.n)
        self.assertEqual(5, self.stack.elements[0])
        with self.assertRaises(ValueError):
            self.fullStack.push(3)

    def test_pop(self):

        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        with self.assertRaises(ValueError):
            self.stack.pop()

    def tearDown(self): pass


if __name__ == '__main__':

    unittest.main()
