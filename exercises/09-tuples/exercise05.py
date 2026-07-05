# Exercise 5: Tuple Methods
# Use .count() and .index() on a tuple.

t = (5, 2, 5, 8, 2, 5, 1, 2, 9, 5)
print(f"Tuple: {t}")

# Count occurrences of each unique value
print(f"Count of 5: {t.count(5)}")
print(f"Count of 2: {t.count(2)}")
print(f"Count of 9: {t.count(9)}")

# Find first occurrence of 5
idx = t.index(5)
print(f"First 5 at index: {idx}")

# Find next 5 after position 3
idx2 = t.index(5, 4)
print(f"Next 5 after index 4 at index: {idx2}")

# Find 5 between positions 2 and 6
idx3 = t.index(5, 2, 6)
print(f"5 between index 2 and 6 at index: {idx3}")

# Handle ValueError gracefully
try:
    t.index(99)
except ValueError:
    print("99 not found in tuple")
