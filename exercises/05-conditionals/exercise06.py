# Exercise 6: Simple Calculator with match/case
# Revisit Exercise 1 from Lesson 4 (Arithmetic Calculator). This time, implement the operator selection using match/case instead of if/elif. Use | to combine /, //, % into one case for the division-by-zero check.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %, **): ")

match op:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "**":
        print(f"{a} ** {b} = {a ** b}")
    case "/" | "//" | "%":
        if b == 0:
            print("Error: Cannot divide by zero!")
        elif op == "/":
            print(f"{a} / {b} = {a / b}")
        elif op == "//":
            print(f"{a} // {b} = {a // b}")
        else:
            print(f"{a} % {b} = {a % b}")
    case _:
        print("Invalid operator!")
