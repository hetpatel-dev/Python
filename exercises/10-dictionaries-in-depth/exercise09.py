# Exercise 9: Counter Deep Dive
# Explore all Counter features.

from collections import Counter

text = "abracadabra"
c = Counter(text)

# Basic count
print(f"Counter: {c}")

# Most common
print(f"Most common 3: {c.most_common(3)}")

# Elements
elements = sorted(c.elements())
print(f"Elements: {elements}")

# Total
print(f"Total: {c.total()}")

# Subtract
c2 = Counter(text)
c2.subtract("alphabet")
print(f"After subtract: {c2}")

# Unary plus — remove non-positive
c3 = +c2
print(f"After unary +: {c3}")

# Counter arithmetic
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2, c=1)
print(f"c1 + c2: {c1 + c2}")
print(f"c1 - c2: {c1 - c2}")
print(f"c1 & c2: {c1 & c2}")
print(f"c1 | c2: {c1 | c2}")
