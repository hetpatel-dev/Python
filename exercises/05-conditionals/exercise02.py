# Exercise 2: Even or Odd + Divisibility
# Ask the user for a number. Print whether it's even or odd, and whether it's divisible by 5 and/or 3. Use the % operator.

# Enter a number: 15
# 15 is odd.
# 15 is divisible by 5 and 3.

# Enter a number: 10
# 10 is even.
# 10 is divisible by 5 but not 3.

try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    if number % 5 == 0:
        print(f"{number} is divisible by 5 but not 3.")
    else:
        print(f"{number} is divisible by 3 but not 5.")
except:
    print("That's not a valid Number.")

# we can even use ternary statements

# print(f"{number} is even.") if number % 2 == 0 else print(
#     f"{number} is odd.")

# print(f"{number} is divisible by 5 but not 3.") if number % 5 == 0 else print(
#     f"{number} is divisible by 3 but not 5.")
