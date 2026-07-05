# Exercise 6: Dict Comprehensions
# Practice various dict comprehension patterns.

# 1. Squares
squares = {x: x**2 for x in range(1, 11)}
print(f"Squares: {squares}")

# 2. Even squares only
even_squares = {x: x**2 for x in range(1, 21) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# 3. Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# 4. Build from two lists with zip
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
gradebook = {name: score for name, score in zip(names, scores)}
print(f"From zip: {gradebook}")

# 5. Filter a dict by value
temperatures = {"London": 15, "Paris": 22, "Moscow": -2, "Sydney": 30}
warm = {city: temp for city, temp in temperatures.items() if temp > 20}
print(f"Warm cities: {warm}")
