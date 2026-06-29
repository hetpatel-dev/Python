# Exercise 5: Type Annotator
# Create a program that asks for the user's name (str), age (int), height in meters (float), and whether they're a student (bool from y/n). Use type annotations on all variables. Print a summary sentence using f-strings that includes the types.

name: str = input("What is your name?: ")
age: int = int(input("How old are you?: "))
height: float = float(input("What is your height? (meters): "))
is_student: bool = input("Are you a student? (y/n): ").lower() == "y"

print(f"Name: {name}    {type(name)}")
print(f"Age: {age}    {type(age)}")
print(f"Height: {height}    {type(height)}")
print(f"Student: {is_student}    {type(is_student)}")

# Output:
# What is your name?: Het
# How old are you?: 22
# What is your height? (meters): 5.5
# Are you a student? (y/n): Y
# Name: Het    <class 'str'>
# Age: 22    <class 'int'>
# Height: 5.5    <class 'float'>
# Student: True    <class 'bool'>
