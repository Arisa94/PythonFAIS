class Stack:
    def __init__(self, size):

        self.elements = []
        self.n = 0
        self.size = size

    def isEmpty(self):

        return self.n == 0

    def isFull(self):

        if self.size == self.n:
            return True
        else:
            return False

    def push(self, data):

        if self.isFull():
            raise ValueError("Stack full!")
        else:
            self.elements.append(data)
            self.n += 1

    def pop(self):

        if self.isEmpty():
            raise ValueError("Stack empty!")
        else:
            self.n -= 1
            temp = self.elements[self.n]
            self.elements[self.n] = None
            return temp
