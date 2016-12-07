from math import *

def heron(a, b, c):
    tmp = [a, b, c]
    tmp.sort()
    if tmp[0] + tmp[1] <= tmp[-1]:
        raise ValueError ("Warunek trojkata jest nie spelniony")
    halfPerimeter = (a + b + c)/2
    return sqrt(halfPerimeter * (halfPerimeter - a)*(halfPerimeter-b)*(halfPerimeter-c))

print heron(7, 4, 3)