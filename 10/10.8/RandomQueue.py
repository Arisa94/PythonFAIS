from random import *


class RandomQueue:

    def __init__(self, size):

        self.size = size
        self.elements = []
        self.end = 0

    def is_full(self):

        return self.size <= self.end

    def insert(self, item):

        if self.is_full():
            raise ValueError("Queue full")
        self.elements.append(item)
        self.end += 1

    def is_empty(self):

        if self.end == 0:
            return True
        else:
            return False

    def remove(self):

        if self.end == 1:
            temp = self.elements[0]
            self.elements[0] = None
        elif self.is_empty():
            raise ValueError("Queue empty")
        else:
            randomIndex = randint(0, self.end-1)
            temp = self.elements[randomIndex]
            self.elements[randomIndex] = self.elements[self.end - 1]
            self.elements[self.end - 1] = None
        self.end -= 1
        return temp

    def printQueue(self):

        for i in self.elements:
            print i

queue = RandomQueue(3)
queue.insert(3)
queue.insert(2)
queue.insert(1)
queue.remove()
queue.printQueue()
