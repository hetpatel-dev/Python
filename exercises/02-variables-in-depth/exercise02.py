# Exercise 2: Mutable Mayhem
# Predict the output before running, then explain why.

# ---------------------------------------------------------------------------
# General rule:
#   =   (assignment)         → rebinds the name to a NEW object
#   .append(), .extend(), etc → MUTATES the existing object in-place
#   +=  (augmented assignment) → MUTATES in-place for mutable types (list),
#                                 but REBINDS for immutable types (int, str)
# ---------------------------------------------------------------------------


# --- BLOCK 1: mutation via method ---

x = [1, 2, 3]
y = x
y.append(4)
print(x)  # [1, 2, 3, 4]

# x and y both reference the SAME list object.
# y.append(4) mutates that shared object in-place.
# Printing x shows the change because x still points to the same (now-changed) object.


# --- BLOCK 2: rebinding via + ---

a = [1, 2, 3]
b = a
b = b + [4]
print(a)  # [1, 2, 3]

# a and b both initially reference [1, 2, 3].
# b + [4] creates a BRAND NEW list [1, 2, 3, 4].
# b = that new list rebinds b to the new object. a still holds the original.
# The key difference: + creates a new object, append() mutates in-place.


# --- BLOCK 3: augmented assignment on immutable type ---

p = 10
q = p
q += 5
print(p)  # 10

# p and q both initially reference the int object 10.
# int is IMMUTABLE, so q += 5 CANNOT modify the existing object.
# Instead, it creates a NEW int object (15) and rebinds q to it.
# p stays pointing at the original 10.

# Contrast with list:
#   list += [4] → MUTATES in-place (doesn't rebind)
#   int  += 5   → REBINDS (can't mutate an immutable)


# Takeaway:
#   Mutable objects (list, dict, set):
#     - Methods like .append() modify the existing object
#     - += modifies in-place
#
#   Immutable objects (int, str, tuple):
#     - Every operation that "changes" the value creates a new object
#     - += rebinds the name to a new object
