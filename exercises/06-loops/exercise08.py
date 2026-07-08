# Exercise 8: Set Intersection Game
# Find intersection/union of two lists using sets, loop over sorted().

a = [3, 7, 2, 9, 5, 7, 3]
b = [5, 8, 2, 1, 9]

common = [str(x) for x in sorted(set(a).intersection(b))]
combined = [str(x) for x in sorted(set(a).union(b))]

print(f"Common numbers (sorted): {", ".join(common)}")
print(f"All unique numbers (sorted): {", ".join(combined)}")
