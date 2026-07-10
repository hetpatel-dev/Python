# Exercise 8: Invoice Generator
# Hardcode item names, quantities, and prices. Use advanced f-strings to format
# a receipt with aligned columns, total at bottom, and currency formatting.

items = [("Widget", 3, 4.99), ("Gadget", 2, 12.50), ("Doohickey", 1, 29.95)]

print(f"{'Item':<10}{'Qty':^6}{'Price':^6}{'Total':>8}")
print(f"{'----':<10}{'---':^6}{'-----':^6}{'-----':>8}")

total = 0

for item in items:
    name, quantity, price = item
    total += (quantity * price)
    print(f"{name:<10}{quantity:^6}{price:^6.2f}{quantity * price:>8.2f}")

print(f"{'----':<10}{'---':^6}{'-----':^6}{'-----':>8}")
print(f"Total: {total:>.2f}")
