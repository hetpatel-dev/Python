# Exercise 3: Single-Element Pitfalls
# Determine which expressions are tuples and which are not.
# Print the type of each.

# Which of these are tuples?
a = (1)
b = (1,)
c = 1,
d = ()
e = ("hello")
f = ("hello",)
g = "hello",

# Print each with type() and repr()
# Example:
print(f"a = {a!r} -> {type(a).__name__}")

# ... print the rest ...

# Bonus: fix this list — it should have 3 points, not 2
# points = [(1, 2), (3, 4)]
# Can you spot the bug?
