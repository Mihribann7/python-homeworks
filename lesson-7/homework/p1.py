import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimension!")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Unsupported operand type for *")

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return sum(a**2 for a in self.components) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Vectors must have magnitude!")
        return self * (1.0 / mag)

    def __repr__(self):
        return f"Vector{self.components}"

    def __str__(self):
        return f"({', '.join(map(str, self.components))})"



v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)

v3 = v1 + v2
print(v3)

v4 = v2 - v1
print(v4)

dot_product = v1 * v2
print(dot_product) 
v5 = 3 * v1
print(v5)
v6 = v1 * 2
print(v6)
print(v1.magnitude())
v_unit = v1.normalize()
print(v_unit)