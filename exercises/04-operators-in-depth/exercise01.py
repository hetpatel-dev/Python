# Exercise 1: Arithmetic Calculator
# Write a program that asks the user for two numbers and an operator
# (+, -, *, /, //, %, **), then prints the result.
# Handle division by zero gracefully with a message.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, //, %, **): ")

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"{a} / {b} = {a / b}")
elif op == "//":
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"{a} // {b} = {a // b}")
elif op == "%":
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"{a} % {b} = {a % b}")
elif op == "**":
    print(f"{a} ** {b} = {a ** b}")
else:
    print("Invalid operator!")
