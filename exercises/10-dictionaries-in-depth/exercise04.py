# Exercise 4: Dict Views & Set Operations
# Use keys() views for set-like operations and demonstrate dynamic nature.

class_a = {"Alice": 90, "Bob": 85, "Charlie": 88}
class_b = {"Bob": 92, "Diana": 95, "Eve": 87}

# Keys views
keys_a = class_a.keys()
keys_b = class_b.keys()

# Set operations on views
both = keys_a & keys_b
only_a = keys_a - keys_b
only_b = keys_b - keys_a
all_students = keys_a | keys_b
exactly_one = keys_a ^ keys_b

print(f"Both classes: {both}")
print(f"Class A only: {only_a}")
print(f"Class B only: {only_b}")
print(f"All students: {all_students}")
print(f"Exactly one: {exactly_one}")

# Demonstrate dynamic nature
print("\n--- Dynamic view demonstration ---")
print(f"Keys A before add: {list(keys_a)}")
class_a["Frank"] = 93
print(f"Keys A after add:  {list(keys_a)}")  # Automatically updated!
