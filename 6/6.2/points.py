from math import *

class Point:

    def __init__(self, x=0, y=0):  
        self.x = x
        self.y = y

    def __str__(self):       
        return str("(" + str(self.x) + ", " + str(self.y) + ")")

    def __repr__(self):       
        return str("Point(" + str(self.x) + ", " + str(self.y) + ")")

    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return True
        else:
            return False

    def __ne__(self, other):
        if(self == other):
            return False;
        else:
            return True;

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  
        return ((self.x * other.x) + (self.y * other.y))

    def cross(self, other):         
        return self.x * other.y - self.y * other.x

    def length(self):         
        return sqrt(pow(self.x, 2) + pow(self.y, 2))
