# Exercise 4: Immutability and Mutable Contents
# Test which operations work and which raise errors.

t = ([1, 2], "hello", 3)
print(f"Before: {t}")
print(f"id(t) = {id(t)}")

# Wrap each operation in try/except and test

# 1. Try t[0] = [99, 100]

# 2. Try t[1] = "world"

# 3. Try t[2] = 99

# 4. Try t[0].append(99)

# 5. Try t[0][0] = 99

# 6. Try del t[0]

# 7. Try del t[0][0]

# 8. Try t += (4,)
print(f"\nAfter t += (4,): {t}")
print(f"id(t) = {id(t)}")
print(f"Same object? {id_before == id(t)}")  # id_before should be saved before the operation
