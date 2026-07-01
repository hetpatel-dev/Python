# Exercise 4: Constructor Explorer
# Take the string "Python" and convert it to each of these types using constructors. Print the result and type for each. Catch any errors with try/except.

# list("Python")
# tuple("Python")
# set("Python")
# bytes("Python", "utf-8")
# dict() — try creating a dict from "Python" and see what error you get

print(list("Python"))
print(tuple("Python"))
print(set("Python"))
print(bytes("Python", "utf-8"))
try:
    print(dict("Python"))
except ValueError as e:
    print(f"dict(\"Python\") raised ValueError: {e}")
