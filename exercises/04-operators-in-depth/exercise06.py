# Exercise 6: Precision Precedence Puzzle
# Without running the code, predict what each expression evaluates to.
# Then uncomment and run to check. Write a brief explanation of the order
# of operations in each case.

# 1. 2 + 3 * 4 - 1
# Prediction: 3 * 4 = 12, then 2 + 12 - 1 = 13
print(2 + 3 * 4 - 1)       # 13

# 2. 2 ** 3 ** 2
# Prediction: ** is right-associative: 2 ** (3 ** 2) = 2 ** 9 = 512
print(2 ** 3 ** 2)         # 512

# 3. 10 - 2 + 3
# Prediction: left to right: (10 - 2) + 3 = 11
print(10 - 2 + 3)          # 11

# 4. 10 - (2 + 3)
# Prediction: parentheses first: 10 - 5 = 5
print(10 - (2 + 3))        # 5

# 5. 8 / 4 * 2
# Prediction: same precedence, left to right: (8 / 4) * 2 = 2 * 2 = 4.0
print(8 / 4 * 2)           # 4.0

# 6. 8 / (4 * 2)
# Prediction: parentheses first: 8 / 8 = 1.0
print(8 / (4 * 2))         # 1.0

# 7. not True and False or True
# Prediction: not True = False, then False and False = False, then False or True = True
print(not True and False or True)  # True

# 8. not (True and False or True)
# Prediction: True and False = False, False or True = True, not True = False
print(not (True and False or True))  # False
