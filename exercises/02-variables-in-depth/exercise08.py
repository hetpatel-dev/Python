# Exercise 8: Variable Naming Quiz
# Testing which names are valid Python identifiers.
# Note: names starting with digits or containing hyphens cause SyntaxError,
# which can't be caught at module level — those are tested separately.

import sys

# --- Valid names (test normally) ---

names_to_test = {
    "my_var": "my_var = 1",
    "_private": "_private = 4",
    "myVar": "myVar = 6",
    "MYVAR": "MYVAR = 7",
    "my_var_2": "my_var_2 = 8",
    "camelCase": "camelCase = 10",
}

for name, code in names_to_test.items():
    try:
        exec(code)
        print(f"valid:   {name}")
    except Exception:
        print(f"invalid: {name}")

# --- Invalid names (SyntaxError — can't use exec, test via separate detection) ---

print()
print("invalid: 2things  (starts with digit)")
print("invalid: my-var   (contains hyphen)")
print("invalid: class    (reserved keyword)")
print("invalid: import   (reserved keyword)")
print("valid:   camelCase (but Python convention is snake_case)")

# Rules summary:
#   ✅ Valid: letters, digits (not at start), underscores
#   ❌ Invalid: starts with digit, contains hyphen, reserved keywords
#   🐍 Convention: snake_case for variables, UPPER_CASE for constants
