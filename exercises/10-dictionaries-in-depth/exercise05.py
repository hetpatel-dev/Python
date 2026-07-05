# Exercise 5: Nested Gradebook
# Work with a nested dict of students -> subjects -> scores.

grades = {
    "Alice": {"Math": 95, "Science": 88, "English": 91},
    "Bob": {"Math": 87, "Science": 92, "English": 85},
    "Charlie": {"Math": 93, "Science": 90, "English": 89},
}

# Print Alice's Math score
print(f"Alice's Math: {grades['Alice']['Math']}")

# Compute per-student averages
print("\nStudent averages:")
for student, subjects in grades.items():
    total = sum(subjects.values())
    count = len(subjects)
    print(f"{student}: {total/count:.1f}")

# Compute class average per subject
print("\nSubject averages:")
subject_totals = {}
for subjects in grades.values():
    for subject, score in subjects.items():
        subject_totals.setdefault(subject, []).append(score)
for subject, scores in subject_totals.items():
    avg = sum(scores) / len(scores)
    print(f"{subject}: {avg:.1f}")

# Add History to each student
for student in grades:
    grades[student]["History"] = 85
print(f"\nAfter adding History: {grades['Alice']}")

# Add Diana
grades["Diana"] = {"Math": 98, "Science": 94, "English": 92, "History": 90}
print(f"Added Diana: {grades['Diana']}")
