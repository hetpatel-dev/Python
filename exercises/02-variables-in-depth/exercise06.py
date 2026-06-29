# Exercise 6: Reference vs Copy

original = [1, 2, [3, 4]]
ref = original
shallow = original[:]  # shallow copy: new outer list, shares nested objects

original[0] = 99
original[2].append(5)

print(f"original: {original}")
print(f"ref:      {ref}")
print(f"shallow:  {shallow}")
print()
print(f"shallow[2] is original[2]: {shallow[2] is original[2]}")  # True!

# Explanation:
#
# original = [1, 2, [3, 4]]
#   original ──→ [1, 2, ●] ──→ [3, 4]
#
# ref = original
#   ref ──→ same object as original (entirely shared)
#
# shallow = original[:]
#   shallow ──→ NEW [1, 2, ●] ──→ same [3, 4] (nested list is still shared)
#
# After original[0] = 99:
#   original ──→ [99, 2, ●]
#   ref      ──→ [99, 2, ●]  (same outer list, sees the change)
#   shallow  ──→ [1, 2, ●]   (different outer list, NOT affected)
#
# After original[2].append(5):
#   The shared nested list [3, 4] becomes [3, 4, 5]
#   All three see the change because they all reference the same nested list:
#   original ──→ [99, 2, [3, 4, 5]]
#   ref      ──→ [99, 2, [3, 4, 5]]
#   shallow  ──→ [1, 2, [3, 4, 5]]
