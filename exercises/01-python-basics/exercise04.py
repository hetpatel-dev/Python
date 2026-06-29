# Exercise 4: Age in Days
# Ask for the user's age in years. Convert to an integer, calculate their approximate age in days (age * 365), and print: "You are approximately [days] days old.".

age = input("How old are you? (years): ")
age_in_days = int(age) * 365
print(f"You are approximately {age_in_days} days old.")

# Output:
# How old are you? (years): 12
# You are approximately 4380 days old.
