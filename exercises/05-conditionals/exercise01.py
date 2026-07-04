# Exercise 1: Number Classifier
# Write a program that asks the user for a number and prints whether it's positive, negative, or zero. Handle the case where the input is not a valid number with a try/except.

# Enter a number: 5
# 5 is positive.

# Enter a number: -3
# -3 is negative.

# Enter a number: 0
# The number is zero.

# Enter a number: abc
# That's not a valid number.


try:
    number = int(input("Enter a number: "))
    if number > 0:
        print(f"{number} is positive.")
    elif number < 0:
        print(f"{number} is negative.")
    else:
        print(f"The number is zero.")
except:
    print("That's not a valid number.")

# point of failure:
# int() function can fail if the provided input is not int
# so to handle program from crash we wrap code inside try/except block
# and on failed conversion print effective statment
