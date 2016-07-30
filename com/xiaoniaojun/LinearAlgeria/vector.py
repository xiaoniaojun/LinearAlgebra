import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return 'Vector:{}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        try:
            if self.dimension != v.dimension:
                raise ValueError
            retVector = [x + y for x, y in zip(self.coordinates, v.coordinates)]
            return retVector
        except ArithmeticError:
            raise ArithmeticError('Can\'t add different dimension vector')

    def __sub__(self, v):
        try:
            if self.dimension != v.dimension:
                raise ValueError
            retVector = [x - y for x, y in zip(self.coordinates, v.coordinates)]
            return retVector
        except ArithmeticError:
            raise ArithmeticError('Can\'t add different dimension vector')

    def __mul__(self, v):
        try:
            if not (isinstance(v, float) or isinstance(v, int)):
                raise TypeError
            retVector = [x * v for x in self.coordinates]
            return retVector
        except TypeError:
            raise TypeError('Not a valid scalar multiple.')

    def magnitude(self):
        magnitudeSquare = 0;
        for x in self.coordinates:
            magnitudeSquare += x**2
        magnitude = math.sqrt(magnitudeSquare)
        return magnitude

#----------------------------------------
a = Vector((7.119,8.215))
b = Vector((-8.233,0.878))
print a*b

