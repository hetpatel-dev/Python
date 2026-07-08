# Exercise 4: Parallel Lists with zip()
# Use zip() to pair students and grades, then search by name.

students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [85, 92, 78, 95]

pairs = list(zip(students, grades))
name = input("Search for a student: ")

found = False
for pair in pairs:
    if pair[0] == name:
        print(f"{name} scored {pair[1]}")
        found = True
        break

if found == False:
    print(f"{name} not found")
