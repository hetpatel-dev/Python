# Exercise 2: Simple Calculator
# Ask the user for two numbers (input() returns strings — you'll need int() to convert). Print their sum, difference, product, and quotient.

# Hint: int("5") converts the string "5" to the integer 5.

number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")

# sum
sum = int(number1) + int(number2)
print(f"{number1} + {number2} = {sum}")

# difference
difference = int(number1) - int(number2)
print(f"{number1} - {number2} = {difference}")

# product
product = int(number1) * int(number2)
print(f"{number1} * {number2} = {product}")

# quotient
quotient = int(number1) / int(number2)
print(f"{number1} * {number2} = {quotient}")


# Output:
# Enter number 1: 24
# Enter number 2: 3
# 24 + 3 = 27
# 24 - 3 = 21
# 24 * 3 = 72
# 24 * 3 = 8.0
