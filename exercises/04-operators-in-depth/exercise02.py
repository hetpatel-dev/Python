# Exercise 2: Grade Classifier with Chained Comparisons
# Ask the user for a numeric grade (0-100) and print the letter grade.
# Use chained comparisons where possible.

grade = float(input("Enter your grade (0-100): "))

if 90 <= grade <= 100:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
elif 0 <= grade < 60:
    print("F")
else:
    print("Invalid grade -- must be between 0 and 100.")
