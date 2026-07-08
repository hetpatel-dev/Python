# loops
# 1. for: iterate over a sequence, use when you know number of iteration in advanced or they are certain
# 2. while: repeat while a condition is true, use when you don't know the number of iteration in advance

# looping over different data types

# list & tuple:
# - direct element access

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit, end=" ")

print()

departments = ("engineering", "design", "sales")
for department in departments:
    print(department, end=" ")

print()

# string
# - direct character access

car = "Mercedes-Gwagon"
for char in car:
    print(char, end=" ")

# dictionary:
# - by default provide keys of each elements (same as dict.keys())
# - dict.keys(): provides keys
# - dict.values(): provides values
# - dict.items(): proides key-value pairs

user = {
    "fname": "Alice",
    "lname": "Hofman"
}

print()

# keys

for key in user:
    print(key, end=" ")

# or

print()

for key in user.keys():
    print(key, end=" ")

# values

print()

for value in user.values():
    print(value, end=" ")

# key-value pairs

print()

for key, value in user.items():
    print(f"{key:^8} {value:^8}")

# sets
# - no proper order
# - different order of elements on each run

numbers = {1, 1, 2, 3, 2, 4, 2, 3, 2, 4, 6, 7}

for number in numbers:
    print(number, end=" ")

# to do sorted looping over sets: sorted()
print()

for number in sorted(numbers):
    print(number, end=" ")


# range(start, stop, step): generate arithmatic sequences, used when need index, but prefer enumerate()

print()

for i in range(10, 1, -2):
    print(i, end=" ")

print()

words = ["cat", "map", "bat"]

for i in range(0, len(words)):
    print(i, words[i])

# while loop

count = 1
while count < 5:
    print(f"Count is: {count}")
    count = count + 1  # this step is imp, otherwise infinite loop

# keep prompting until valid input

# while True:
#     reply = input("Type 'quit' to exit: ")
#     if reply == "quit":
#         break
#     print(f"You said: {reply}")

# break exits the innermost loop immediately

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} * {n//x}")
            break

# continue: skips the rest of the current iteration and moves to the next one:

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Even: {num}")
        continue   # skip exectuing rest of the below code for even number iteration
    print(f"Odd: {num}")

# A loop's else clause runs when the loop finishes normally: when not terminated by break

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} * {n // x}")
            break

    else:
        print(f"{n} is a prime number")

# The else belongs to the for (or while), not the if. Think of it as: "run this if no break happened."

n = 0
while n < 5:
    n += 1
    # print(n)
    if n == 3:
        break
else:
    print("Completed without break")  # won't run — break at 3

# enumerate() adds a counter to an iterable. It yields (index, value) tuples:

seasons = ["Summer", "Winter", "Fall", "Spring"]
for i, season in enumerate(seasons):
    print(f"{i} : {season}")

foods = ["chineese", "indian", "italian", "germen"]
for i, food in enumerate(foods, start=1):
    print(f"{i} : {food}")

# zip(): zip() pairs elements from two or more iterables, stopping at the shortest one:

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for score, name in zip(scores, names):
    print(f"{score:<6}{name:<6}")


# nested loop

for row in range(0, 3):
    for col in range(0, 3):
        print(f"({row}, {col})", end=" ")
    print()

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()

# reversed() — Loop in Reverse

for i in reversed(range(1, 11)):
    print(i, end=" ")

print()

for ch in reversed("Hello"):
    print(ch, end=" ")

print()

# sorted() — Loop in Sorted Order

# for fruit in sorted(["apple", "pinaple", "graps", "banana", "cherry"]):
#     print(fruit)

basket = ["apple", "orange", "apple", "pear", "orange",
          "apple", "pinaple", "graps", "banana", "cherry"]

# sorted() returns a new list without modifying the original. Combine with set() to loop over unique elements in order:

for fruit in sorted(set(basket)):
    print((fruit))
