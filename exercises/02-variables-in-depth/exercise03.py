# Exercise 3: Swap Without Temp
# Create two variables a = 5 and b = 10. Swap their values using Python's tuple unpacking (one line). Print before and after. Then verify with the user (the program asks the user for two numbers, swaps them, and prints the result).

a = 5
b = 10

print("before swaping a: ", a)
print("before swaping b: ", b)

a, b = b, a
# right side will be computed first then assignment will take place replacing values

print("after swaping a: ", a)
print("after swaping b: ", b)


number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

print("before swaping a: ", number1)
print("before swaping b: ", number2)

number1, number2 = number2, number1
# right side will be computed first then assignment will take place replacing values

print("after swaping a: ", number1)
print("after swaping b: ", number2)
