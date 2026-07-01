# Exercise 5: Type Checker

value = input("Enter a value: ")

try:
    int(value)
    print("That's an integer!")
except ValueError:
    try:
        float(value)
        print("That's a float!")
    except ValueError:
        print("That's a string!")
