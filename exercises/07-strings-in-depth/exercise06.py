# Exercise 6: Password Validator
# Ask user for a password. Check: at least 8 chars, has uppercase, has lowercase,
# has digit, has special char. Use isupper(), islower(), isdigit(), and a set of
# special characters. Report which checks passed/failed.

password = input("Enter password: ").strip()

if 0 < len(password) < 8:
    print(f"❌ Too short ({len(password)} chars, need at least 8)")
elif len(password) == 8:
    print(f"✅ Pass ({len(password)} chars, matches at least 8)")
elif len(password) > 8:
    print(f"✅ Pass ({len(password)} chars, matches at least 8)")
else:
    print("❌ Invalid Password!")

for character in password:
    if character.isupper():
        print(f"Uppercase: ✅ Pass")
        break
else:
    print(f"Uppercase: ❌ Fail")

for character in password:
    if character.islower():
        print(f"Lowercase: ✅ Pass")
        break
else:
    print(f"Lowercase: ❌ Fail")

for character in password:
    if character.isdigit():
        print(f"Digit: ✅ Pass")
        break
else:
    print(f"Digit: ❌ Fail")

for character in password:
    if character in ("!", "@", "#", "$", "."):
        print(f"Special: ✅ Pass")
        break
else:
    print(f"Spcial: ❌ Fail")
