# Exercise 2: Truthiness Tester
# Create a list of 10 different values of different types (including 0, "", [], None, "text", [1], etc.). Loop through them and print:

# Value: 0 → bool: False
# Value: "hello" → bool: True

values = [0, 10, "helllo", "", [], [0],
          (10, 20), (), {"message": "hello"},  {}, {1, 2, 3, 4, 3, 2, 2, 1}, 0.0, 12.2, 0 + 0j, 1 + 1j, None, False, True]

for value in values:
    print(f"Value: {value} -> bool: {bool(value)}")

# Output:
# Value: 0 -> bool: False
# Value: 10 -> bool: True
# Value: helllo -> bool: True
# Value:  -> bool: False
# Value: [] -> bool: False
# Value: [0] -> bool: True
# Value: (10, 20) -> bool: True
# Value: () -> bool: False
# Value: {'message': 'hello'} -> bool: True
# Value: {} -> bool: False
# Value: {1, 2, 3, 4} -> bool: True
# Value: 0.0 -> bool: False
# Value: 12.2 -> bool: True
# Value: 0j -> bool: False
# Value: (1+1j) -> bool: True
# Value: None -> bool: False
# Value: False -> bool: False
# Value: True -> bool: True
