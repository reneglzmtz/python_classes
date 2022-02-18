class Point:
    default_color = "red"

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point.x)
print(point.default_color)
Point.default_color = "yellow"
print(Point.default_color)
point.draw()
print(point)

another = Point.zero()
another.draw()
another = Point(3, 4)
print(point == another)

print(point > another)
print(point < another)
print(point + another)