# Exercise 6: is vs isinstance
# Create value = True. Then test:

# type(value) is int — print the result
# isinstance(value, int) — print the result
# They differ! Explain in a comment why. (Hint: bool is a subclass of int.)

value = True

print(type(value) is int)  # bool and int object are not same
print(type(value).__name__)  # bool, we were comparing against int

print(isinstance(value, int))

# type(value) function gives data type of given value.
# isinstance(value, [type, [...types]]) function validates whether value provided is of given class and it's subclass or not.

# type() function returns the string containg type of the value
# isinstance() function returns boolean True or False
