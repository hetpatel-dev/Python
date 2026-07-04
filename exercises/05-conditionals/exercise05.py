# Exercise 5: Shipping Calculator
# Write a program that calculates shipping cost based on order total and distance:

# Orders over $50 ship free
# Orders $25-$50: $5 flat + $0.50 per km
# Orders under $25: $3 flat + $1.00 per km
# If the shipping cost exceeds the order total, print "Shipping is more than the item value!" instead of the cost.

# Enter order total: 100
# Shipping is free! Total: $100.00

# Enter order total: 30
# Enter distance (km): 10
# Shipping cost: $10.00. Total: $40.00

# Enter order total: 15
# Enter distance (km): 20
# Shipping is more than the item value!


# order_total = int(input("Enter order total: "))

# if order_total > 50:
#     print(f"Shipping is free! Total: ${order_total:.2f}")

# if 25 <= order_total <= 50:
#     distance = float(input("Enter distance (km): "))
#     flat_shipping_fee = 5
#     per_km_shipping_fee = 0.50
#     shipping_cost = flat_shipping_fee + (distance * per_km_shipping_fee)
#     total = order_total + shipping_cost

#     if shipping_cost > order_total:
#         print("Shipping is more than the item value!")
#     else:
#         print(f"Shipping cost: ${shipping_cost:.2f}. Total: ${total:.2f}")

# if order_total < 25:
#     distance = float(input("Enter distance (km): "))
#     flat_shipping_fee = 3
#     per_km_shipping_fee = 1.00
#     shipping_cost = flat_shipping_fee + (distance * per_km_shipping_fee)
#     total = order_total + shipping_cost

#     if shipping_cost > order_total:
#         print("Shipping is more than the item value!")
#     else:
#         print(f"Shipping cost: ${shipping_cost:.2f}. Total: ${total:.2f}")

order_total = int(input("Enter order total: "))

if order_total > 50:
    shipping_cost = 0
elif order_total >= 25:
    distance = float(input("Enter distance (km): "))
    shipping_cost = 5 + distance * 0.50
else:
    distance = float(input("Enter distance (km): "))
    shipping_cost = 3 + distance * 1.00

if shipping_cost == 0:
    print(f"Shipping is free! Total: ${order_total:.2f}")
elif shipping_cost > order_total:
    print("Shipping is more than the item value!")
else:
    total = order_total + shipping_cost
    print(f"Shipping cost: ${shipping_cost:.2f}. Total: ${total:.2f}")
