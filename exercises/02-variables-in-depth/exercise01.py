# Exercise 1: Identity Explorer
# Demonstrates object identity — understanding when variables share objects vs get new ones

a = 256
b = 256
print(f"a is b (a={a}, b={b}): {a is b}")  # True

# Why True? Python pre-allocates integer objects for -5 to 256 at startup.
# Any variable assigned 256 gets a reference to the SAME pre-existing object.
# This is a CPython optimization — don't rely on it in production code.

c = 257
d = 257
# True in a script, may differ in REPL
print(f"c is d (c={c}, d={d}): {c is d}")

# This is True in a SCRIPT because Python's compiler folds identical
# constant literals into one object within the same compilation unit.
# In the REPL, each line is compiled separately, so c = 257 and d = 257
# on separate lines would give False.
# Outside the -5 to 256 range, NOTHING is guaranteed about object reuse.
# The "may differ!" note refers to cross-version/interpreter differences.

e = "hello"
f = "hello"
print(f"e is f (e='{e}', f='{f}'): {e is f}")  # True

# True because of string interning: CPython reuses short string literals
# that look like identifiers (no spaces, simple characters).
# The str type is immutable, so reusing is safe and saves memory.
# Again, rely on == for string comparison, not is.

g = [1, 2]
h = [1, 2]
print(f"g is h (g={g}, h={h}): {g is h}")  # False

# False because list literals ALWAYS create a new list object.
# Lists are mutable, so Python can't safely share them.
# Even with identical contents, each [] creates a separate object.

# Key takeaway:
#   ==  compares VALUE — use this for meaningful comparisons
#   is  compares IDENTITY — use this only for None checks and sentinels
#   id() reveals the memory address — useful for debugging, not production
#   Mutable types (list, dict, set) always create new objects with [], {}
#   Immutable types (int, str) may or may not reuse objects - never asuume
