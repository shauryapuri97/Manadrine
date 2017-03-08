import math

class Vector:

    def __init__(self, p=(0, 0)):
        self.x = p[0]
        self.y = p[1]

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def getP(self):
        return (self.x, self.y)

    def copy(self):
        x = self.x
        y = self.y

        return (x, y)

    def mult(self, k):
        self.x = self.x * k
        self.y = self.y * k

    def div(self, k):
        self.x = self.x / k
        self.y = self.y / k

    def normalise(self):
        return self.div(self.length())

    def get_normalised(self):
        v = Vector(self.copy())
        v.div(v.length())
        return v

    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def sub(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y

    def negate(self):
        self.x = -self.x
        self.y = -self.y

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def length_squared(self):
        return math.pow(self.x, 2) + math.pow(self.y, 2)

    def reflect(self, normal):
        n = normal.copy()
        n.mult(2 * self.dot(normal))
        self.sub(n)
        return self

    def angle(self, other):
        dot = self.dot(other)
        length_product = self.length() * other.length()
        return math.degrees(math.acos(dot / length_product))

v = Vector((10, 5))
u = Vector((7, 7))

print v
print v.get_normalised()
print v.angle(u)
