# Exercise 5: Table Formatter
# Hardcode a list of (name, score) tuples. Display them as a right-aligned table
# using rjust()/ljust()/center() so columns line up neatly.

student_score = [("Alice", 95), ("Bob", 82), ("Charlie", 91), ("Diana", 88)]

print(f"{'Name'.ljust(8)} {'Score'.ljust(5)}")
print(f"{'----'.ljust(8)} {'-----'.ljust(5)}")

for student, score in student_score:
    print(f"{student.rjust(8)} {str(score).rjust(5)}")
