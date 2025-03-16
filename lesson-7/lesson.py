import math
#import this


"""point1 = (3, 4)
point2 = (16, 8)

circle_center = (5, 5)
circle_radius = 5

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def is_inside_circle(circle_center, circle_radius, point):
    return distance(circle_center, point) <= circle_radius
"""

# int -> class, 5 -> obj


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def distance(self, p2):
    #    return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

    def test(self):
        print("Hello")

    def add_5_to_x(self):
        return self.x + 5

"""
c = Point(2, 3)
d = Point(4, 5)
print(c.distance(d))
print(c.x, c.y)
c.test()
print(c.add_5_to_x())
"""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        print("Executed")
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector2D(new_x, new_y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __call__(self):
        return "Object called"

v1 = Vector2D(3, 4)
v2 = Vector2D(3, 4)
v3 = v1 + v2

if v1 == v2:
    print("Equal")
else:
    print("Not equal")
print(v3)


















"""a = Point()
a.x = 5 # attribute - instance variable
a.y = 6

b = Point()
b.x = 5
b.y = 6
#print(a.x, a.y)

# x : int = 5

def distance(p1: Point, p2: Point):
    return math.sqrt((p1.x - p1.y)**2  + (p2.x - p2.y)**2)

print(distance(a, b))"""