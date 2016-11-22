class Frac:

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):
        if not(self.y == 1):
            return str(self.x) + '/' + str(self.y)
        else:
            return str(self.x)

    def __repr__(self):
        return str("Frac(" + str(self.x) + ", "+str(self.y) + ")")

    def __add__(self, other):
        return Frac((self.x * other.y) + (other.x * self.y) , self.y * other.y)

    def __sub__(self, other):
        return Frac((self.x * other.y) - (other.x * self.y) , self.y * other.y)

    def __mul__(self, other):
        return Frac(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Frac(self.x * other.y, self.y * other.x);

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __cmp__(self, other):
        tmp1 = float(self)
        tmp2 = float(other)
        if tmp1 == tmp2:
            return 0
        if tmp1 > tmp2:
            return 1
        else:
            return -1

    def __float__(self):
        return float(self.x) / float(self.y)
