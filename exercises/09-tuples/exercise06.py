# Exercise 6: Tuple Operations
# Demonstrate concatenation, repetition, membership, and other operations.

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
print(f"t1 + t2 = {t1 + t2}")

# Repetition
print(f"t1 * 4 = {t1 * 4}")

# Membership
print(f"3 in t1 = {3 in t1}")

# Length
print(f"len(t1) = {len(t1)}")

# Min, Max, Sum
print(f"min(t1)={min(t1)}, max(t1)={max(t1)}, sum(t1)={sum(t1)}")

# Slicing
print(f"First 2: {t1[:2]}, Last 2: {t1[-2:]}, Reversed: {t1[::-1]}")

# Quadratic concatenation demo — build a loop vs list
import time

# BAD: building tuple with += in a loop
start = time.perf_counter()
result = ()
for x in range(10000):
    result += (x,)
slow_time = time.perf_counter() - start
print(f"Tuple += loop: {slow_time:.4f}s (length={len(result)})")

# GOOD: building a list, then converting
start = time.perf_counter()
result = []
for x in range(10000):
    result.append(x)
result = tuple(result)
fast_time = time.perf_counter() - start
print(f"List + tuple(): {fast_time:.4f}s (length={len(result)})")

print(f"Speedup: {slow_time / fast_time:.1f}x")
