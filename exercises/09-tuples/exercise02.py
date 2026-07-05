# Exercise 2: Starred Unpacking
# Use the * operator to capture multiple items during unpacking.

numbers = list(range(1, 11))
print(f"Numbers: {numbers}")

# Extract first, rest (as a list), and last
first, *rest, last = numbers
print(f"first={first}, rest={rest}, last={last}")

# Extract first, second, rest, last
items = [1, 2, 3, 4, 5, 6, 7]


print(f"first={first}, second={second}, rest={rest}, last={last}")

# Starred unpacking with only 2 items (middle should be empty)
two = [1, 2]


print(f"With 2 items: first={first}, middle={middle}, last={last}")
