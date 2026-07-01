# Exercise 4: Membership & Identity Challenge
# Given these variables, write expressions using `in`, `not in`, `is`, `is not`
# that evaluate to True for each description below.

text = "hello world"
numbers = [1, 2, 3, 4, 5]
person = {"name": "Alice", "age": 30, "city": "Paris"}
my_list = [1, 2, 3]
same_list = my_list
other_list = [1, 2, 3]

# 1. Check if 'w' is in text
print("w" in text)

# 2. Check if 6 is NOT in numbers
print(6 not in numbers)

# 3. Check if "age" is a key in person
print("age" in person)

# 4. Check if "Alice" is a value in person (remember: `in` checks keys!)
print("Alice" in person.values())

# 5. Check if my_list and same_list are the SAME object
print(my_list is same_list)

# 6. Check if my_list and other_list are NOT the same object
print(my_list is not other_list)

# 7. Check if my_list and other_list have the SAME value
print(my_list == other_list)

# 8. BONUS: What if we check if None is the same as itself? Write it.
print(None is None)
