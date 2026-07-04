# Exercise 3: Vowel or Consonant
# Ask the user for a single letter. Use a match/case statement with the | operator to print whether it's a vowel or consonant. Handle uppercase and lowercase. If it's not a letter at all, print an error.

# Enter a letter: a
# a is a vowel.

# Enter a letter: B
# B is a consonant.

# Enter a letter: 5
# That's not a letter.

letter = input("Enter a letter: ")

if not letter.isalpha() or len(letter) != 1:
    print("That's not a letter.")
else:
    match letter.lower():
        case "a" | "e" | "i" | "o" | "u":
            print(f"{letter} is a vowel.")
        case _:
            print(f"{letter} is a consonant.")
