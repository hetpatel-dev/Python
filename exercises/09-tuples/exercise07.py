# Exercise 7: Lexicographic Comparison
# Sort tuples and use tuple comparison for multi-key sorting.

coordinates = [(4, 1), (2, 3), (2, 2), (1, 5), (3, 4)]
print(f"Coordinates: {coordinates}")

# Default sort (by first element, then second)
sorted_default = sorted(coordinates)
print(f"Sorted (default): {sorted_default}")

# Sort by second element only
sorted_by_y = sorted(coordinates, key=lambda p: p[1])
print(f"Sorted by y: {sorted_by_y}")

# Sort by y descending, then x ascending
sorted_complex = sorted(coordinates, key=lambda p: (-p[1], p[0]))
print(f"Sorted by y desc, x asc: {sorted_complex}")

# Multi-key sort with student data
students = [("Bob", 20, 88), ("Alice", 22, 95), ("Charlie", 20, 88)]
print(f"\nStudents: {students}")

# Sort by score descending, then name ascending
sorted_students = sorted(students, key=lambda s: (-s[2], s[0]))
print(f"Sorted by score desc, name asc: {sorted_students}")
