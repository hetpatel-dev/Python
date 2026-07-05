# Exercise 8: Grouping with defaultdict
# Group items by category using defaultdict and setdefault.

from collections import defaultdict

data = [
    ("fruit", "apple"), ("fruit", "banana"), ("fruit", "cherry"),
    ("vegetable", "carrot"), ("vegetable", "broccoli"),
    ("fruit", "date"), ("dairy", "milk"), ("dairy", "cheese"),
    ("vegetable", "spinach"),
]

# 1. defaultdict(list)
grouped = defaultdict(list)
for category, item in data:
    grouped[category].append(item)

print("With defaultdict(list):")
for category, items in grouped.items():
    print(f"{category}: {items}")

# 2. Plain dict + setdefault()
grouped2 = {}
for category, item in data:
    grouped2.setdefault(category, []).append(item)

print("\nWith setdefault():")
for category, items in grouped2.items():
    print(f"{category}: {items}")

# 3. Bonus: defaultdict(set) for deduplication
data_with_dupes = data + [("fruit", "apple"), ("dairy", "milk")]
grouped3 = defaultdict(set)
for category, item in data_with_dupes:
    grouped3[category].add(item)

print("\nBonus — deduplicated with defaultdict(set):")
for category, items in grouped3.items():
    print(f"{category}: {items}")
