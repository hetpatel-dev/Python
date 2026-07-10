# Exercise 2: Username Normalizer
# Ask the user for their full name. Normalize it: strip whitespace, lowercase,
# replace spaces with underscores, and ensure no leading/trailing special chars.

# steps
# 1. take input
# 2. strip whitespaces from start and end
# 3. convert to lowercase
# 4. split string into words
# 5. join words by underscore
# 6. remove special characters "!@#$%^&*(){}[]:<>?/;'\\|/"

fullname = "_".join(input("Enter your full name: ").strip(
).lower().split()).strip("!@#$%^&*(){}[]:<>?/;'\\|/")

print(f"Normalized: {fullname}")


