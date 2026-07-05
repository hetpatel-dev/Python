# Exercise 9: Named Tuples
# Define and use named tuples for structured data.

from collections import namedtuple
import math

# Define a Point named tuple


# Create points
p1 = Point(3, 4)
p2 = Point(0, 0)
print(f"p1 = {p1}")
print(f"p2 = {p2}")

# Compute Euclidean distance
def distance(p, q):
    ...

print(f"Distance p1 to p2: {distance(p1, p2)}")

# ._asdict()
print(f"p1 as dict: {p1._asdict()}")

# ._replace() — move by an offset
p1_moved = p1._replace(x=p1.x + 1, y=p1.y - 1)
print(f"p1 moved by (1, -1): {p1_moved}")

# Define a Circle named tuple containing a Point center
Circle = namedtuple("Circle", ["center", "radius"])
c = Circle(center=Point(1, 1), radius=5)
print(f"\nc = {c}")
print(f"Circle area: {math.pi * c.radius ** 2:.2f}")

# _make() from a list
p3 = Point._make([7, 8])
print(f"\nFrom list: {p3}")
