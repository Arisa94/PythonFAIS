class Queue:

    def __init__(self, size):

        self.size = size
        self.elements = []

    def isEmpty(self):

        if self.elements:
            return False
        else:
            return True

    def isFull(self):

        if len(self.elements) == self.size:
            return True
        else:
            return False

    def put(self, data):

        if self.isFull():
            raise ValueError("Queue full!")
        else:
            self.elements.append(data)

    def get(self):

        if self.isEmpty():
            raise ValueError("Queue empty!")
        else:
            return self.elements.pop(0)