# Exercise 10: Mixed Review — CSV Parsing with Dictionaries
# Parse CSV strings into nested dicts, use Counter, defaultdict.

from collections import Counter, defaultdict

data = [
    "Alice,Math,95,20",
    "Bob,Science,87,19",
    "Charlie,Math,92,21",
    "Alice,Science,88,20",
    "Bob,Math,90,19",
    "Charlie,English,85,21",
    "Diana,Math,98,20",
    "Diana,Science,94,20",
]

# Parse into nested dict: {name: {subject: (score, age)}}
records = {}
for line in data:
    name, subject, score_str, age_str = line.split(",")
    score = int(score_str)
    age = int(age_str)
    records.setdefault(name, {})[subject] = (score, age)

print("Nested dict:")
for name, subjects in records.items():
    print(f"{name}: {subjects}")

# Most popular subject (by number of entries)
subject_counter = Counter()
for subjects in records.values():
    for subject in subjects:
        subject_counter[subject] += 1
most_popular = subject_counter.most_common(1)[0]
print(f"\nMost popular subject: {most_popular[0]} ({most_popular[1]} entries)")

# Group scores by subject
scores_by_subject = defaultdict(list)
for subjects in records.values():
    for subject, (score, _) in subjects.items():
        scores_by_subject[subject].append(score)

print("\nSubject averages:")
for subject, scores in sorted(scores_by_subject.items()):
    avg = sum(scores) / len(scores)
    print(f"{subject}: {avg:.2f}")

# Student with highest total score
student_totals = {}
for name, subjects in records.items():
    total = sum(score for score, _ in subjects.values())
    student_totals[name] = total

top_student = max(student_totals, key=student_totals.get)
print(f"\nHighest total score: {top_student} ({student_totals[top_student]})")
