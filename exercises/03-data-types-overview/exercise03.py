# Exercise 3: Mutable vs Immutable Sorter

types_to_check = [42, "hello", [1, 2], (3, 4), {1, 2},
                  {"a": 1}, b"bytes", bytearray(b"abc"), True, None]

immutable_types = (int, float, complex, str, bool, tuple,
                   frozenset, bytes, range, type(None))
mutable_types = (list, dict, set, bytearray, memoryview)

for value in types_to_check:
    t = type(value)
    if t in immutable_types:
        print(f"{t.__name__:12} -> immutable")
    elif t in mutable_types:
        print(f"{t.__name__:12} -> mutable")
    else:
        print(f"{t.__name__:12} -> unknown")

# int          -> immutable
# str          -> immutable
# list         -> mutable
# tuple        -> immutable
# set          -> mutable
# dict         -> mutable
# bytes        -> immutable
# bytearray    -> mutable
# bool         -> immutable
# NoneType     -> immutable
