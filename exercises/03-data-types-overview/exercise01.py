# Exercise 1: Type Catalog
# Create a .py file that creates one example of each built-in type listed below. Use print(f"{name}: {value} → {type(value)}") for each.

# Types to include: int, float, complex, bool, str, bytes, bytearray, list, tuple, range, set, frozenset, dict, NoneType.

# numeric type

int_data = 50
float_data = 40.99
complex_data = 5 + 4j

print(f"Integer: {int_data} -> {type(int_data)}")
print(f"Float: {float_data} -> {type(float_data)}")
print(f"Complex: {complex_data} -> {type(complex_data)}")

# boolean type

bool_data = True
print(f"Boolean: {bool_data} -> {type(bool_data)}")

# string type

str_data = "Hello"
print(f"String: {str_data} -> {type(str_data)}")

# binary types: bytes, bytearray

bytes_data = b"Hello, World!"
bytes_array_data = bytearray(bytes_data)

print(f"Bytes: {bytes_data} -> {type(bytes_data)}")
print(f"Bytes Array: {bytes_array_data} -> {type(bytes_array_data)}")

# sequence types: list, tuple, range

list_data = ["apple", "banana", "mango"]
tuple_data = (100, 200)
range_data = range(0, 10, 2)

print(f"List: {list_data} -> {type(list_data)}")
print(f"Tuple: {tuple_data} -> {type(tuple_data)}")
print(f"Range: {range_data} -> {type(range_data)}")

# set types: set, frozen set

set_data = {1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7}
frozenset_data = frozenset(set_data)

print(f"Set: {set_data} -> {type(set_data)}")
print(f"Frozen Set: {frozenset_data} -> {type(frozenset_data)}")

# mappings type: dict

dict_data = {
    "topic": "Data Types Overview",
    "types_covered": 14
}

print(f"Dictionary: {dict_data} -> {type(dict_data)}")

# None Type

none_data = None
print(f"None: {none_data} -> {type(none_data)}")


# Output:

# Integer: 50 -> <class 'int'>
# Float: 40.99 -> <class 'float'>
# Complex: (5+4j) -> <class 'complex'>
# Boolean: True -> <class 'bool'>
# String: Hello -> <class 'str'>
# Bytes: b'Hello, World!' -> <class 'bytes'>
# Bytes Array: bytearray(b'Hello, World!') -> type(bytes_array_data)
# List: ['apple', 'banana', 'mango'] -> <class 'list'>
# Tuple: (100, 200) -> <class 'tuple'>
# Range: range(0, 10, 2) -> <class 'range'>
# Set: {1, 2, 3, 4, 5, 6, 7} -> <class 'set'>
# Frozen Set: frozenset({1, 2, 3, 4, 5, 6, 7}) -> <class 'frozenset'>
# Dictionary: {'topic': 'Data Types Overview', 'types_covered': 14} -> <class 'dict'>
# None: None -> <class 'NoneType'>
