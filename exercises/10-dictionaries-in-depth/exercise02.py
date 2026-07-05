# Exercise 2: Dict Methods Lab
# Demonstrate pop, popitem, setdefault, update, and fromkeys (with trap).

d = {"a": 1, "b": 2, "c": 3}
print(f"Original dict: {d}")

# 1. pop("b")
val = d.pop("b")
print(f"After pop('b'): {val}, dict={d}")

# 2. popitem() — LIFO
key, val = d.popitem()
print(f"After popitem(): ('{key}', {val}), dict={d}")

# 3. setdefault
d2 = {"a": 1}
val1 = d2.setdefault("x", 99)
print(f"After setdefault('x', 99): {val1}, dict={d2}")
val2 = d2.setdefault("a", 0)
print(f"After setdefault('a', 0): {val2} (key exists, unchanged)")

# 4. update
d2.update({"y": 10, "z": 20})
print(f"After update: {d2}")

# 5. fromkeys mutable default trap
keys = ["p", "q", "r"]
d3 = dict.fromkeys(keys, [])
d3["p"].append(99)
print(f"fromkeys trap: {d3}")

# Fix with dict comprehension
d4 = {k: [] for k in keys}
d4["p"].append(99)
print(f"Comprehension fix: {d4}")
