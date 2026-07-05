# Exercise 8: Composite Dict Keys
# Use tuples as dictionary keys for a gradebook.

grades = {}

# Add entries with (student, subject) tuple keys
# e.g., grades[("Alice", "Math")] = 95


# Print Alice's Math score
print(f"Alice's Math score: {grades[('Alice', 'Math')]}")

# Print all entries as "Student | Subject | Score"
print("\nAll grades:")
# ...

# Calculate and print each student's average
print("\nAverages:")
# ...

# Try using a list as a key — what happens?
print("\nTrying list as key...")
try:
    # grades[["Alice", "History"]] = 90
    pass
except TypeError as e:
    print(f"TypeError: {e}")
