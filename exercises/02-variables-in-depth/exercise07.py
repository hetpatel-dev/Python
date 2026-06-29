# Exercise 7: String Immutability
# Write a script that demonstrates strings are immutable:

# - Assign word = "hello"
# - Show that word[0] = "H" raises an error (wrap in try/except)
# - Create a new string by slicing: word = "H" + word[1:]
# - Print the original and new — show that id() changes

word = "hello"

try:
    word[0] = "H"
except TypeError:
    print("Can't Modify String, it's immutable")

print("original: ", word, id(word))
word = "H" + word[1:]
print("new: ", word, id(word))
