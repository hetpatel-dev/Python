# Exercise 4: Star Unpacking
# Given the list numbers = [10, 20, 30, 40, 50], use star unpacking to:

#   - Assign the first number to first, the rest to rest
#   - Assign the last number to last, everything before to head
#   - Assign the first to start, last to end, everything between to middle
#   - Print all variables to verify.

numbers = [10, 20, 30, 40, 50]

# Assign the first number to first, the rest to rest
first, *rest = numbers
print(first, rest)  # Output: 10 [20, 30, 40, 50]


# Assign the last number to last, everything before to head
*head, last = numbers
print(head, last)  # Output: [10, 20, 30, 40] 50

# Assign the first to start, last to end, everything between to middle
start, *middle, end = numbers

print(start, middle, end)  # 10 [20, 30, 40] 50
