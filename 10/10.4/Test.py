from Queue import *
import unittest


class Test(unittest.TestCase):

    def setUp(self):

        self.emptyQueue = Queue(5)
        self.queue = Queue(3)
        self.fullQueue = Queue(1)
        self.fullQueue.put(1)

    def test_init(self):

        self.temp = Queue(2)
        self.assertEqual(self.temp.size, 2)

    def test_isEmpty(self):

        self.assertTrue(self.emptyQueue.isEmpty())
        self.assertTrue(self.queue.isEmpty())
        self.assertFalse(self.fullQueue.isEmpty())

    def test_isFull(self):

        self.assertFalse(self.emptyQueue.isFull())
        self.assertFalse(self.queue.isFull())
        self.assertTrue(self.fullQueue.isFull())

    def test_put(self):

        self.queue.put(3)
        self.assertEqual(self.queue.elements[0], 3)
        with self.assertRaises(ValueError):
            self.fullQueue.put(5)

    def test_get(self):

        self.queue.put(3)
        self.assertEqual(self.queue.get(), 3)
        with self.assertRaises(ValueError):
            self.queue.get()

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  