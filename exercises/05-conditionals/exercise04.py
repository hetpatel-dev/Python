# Exercise 4: Ternary — Discount Calculator
# Ask the user for the purchase amount and whether they're a member ("yes" or "no"). Use a ternary expression to set the discount: 15% for members, 5% for non-members. Print the final price.

# Enter amount: 200
# Are you a member? (yes/no): yes
# Final price: $170.00

# Enter amount: 200
# Are you a member? (yes/no): no
# Final price: $190.00

purchase_amount = int(input("Enter amount: "))
is_member = input("Are you member? (yes/no): ").strip()

final_price = purchase_amount - \
    (purchase_amount * 0.15) if is_member == "yes" else purchase_amount - \
    (purchase_amount * 0.05)

print(f"Final price: ${final_price}")
