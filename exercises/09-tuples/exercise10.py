# Exercise 10: Mixed Review — CSV Parsing and Data Analysis
# Parse CSV strings into tuples, analyze, and convert to named tuples.

from collections import namedtuple

data = [
    "Alice,Math,95,20",
    "Bob,Science,87,19",
    "Charlie,Math,92,21",
    "Alice,Science,88,20",
    "Bob,Math,90,19",
    "Charlie,English,85,21",
]

# Parse each string into a (name, subject, score, age) tuple
records = []


print("Parsed records:")
for r in records:
    print(f"  {r}")

# Find the highest score
highest = max(records, key=lambda r: r[2])
print(f"\nHighest score: {highest[2]} ({highest[0]}, {highest[1]})")

# Create a dict with (name, subject) tuple keys
gradebook = {}


print("\nGradebook lookup:")
print(f"  Alice's Math: {gradebook[('Alice', 'Math')]}")

# Define a StudentRecord named tuple
StudentRecord = namedtuple("StudentRecord", ["name", "subject", "score", "age"])

# Convert each tuple to a named tuple


print("\nAs named tuples:")
# ...

# Sort by score descending
sorted_records = sorted(records, key=lambda r: r[2], reverse=True)
print("\nSorted by score (desc):")
for r in sorted_records:
    print(f"  {r[0]} | {r[1]} | {r[2]}")
