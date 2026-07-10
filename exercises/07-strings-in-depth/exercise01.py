# Exercise 1: String Slicer
# Given a hardcoded string, extract and print various slices using [start:stop:step].

# first 6 characters, last 11 characters, every 2nd character, the string reversed, and the middle 5 characters using negative indices.

text = "Python Programming"

# first 6 characters
print("First 6:", text[0:6])  # Python

# last 11 characters
print("Last 11:", text[-11:])  # Programming

# every second character
print("Every 2nd:", text[::2])  # Pto rgamn

# the string reversed
print("Reversed String:", text[::-1])  # gnimmargorP nohtyP

# find middle 5 characters in string
middle_count = 5
start = (len(text) - middle_count) // 2
stop = start + middle_count

print("Middle 5:", text[start:stop])  # " Prog"

# logic for any string and any number of middle characters. The formula is:
# start = (length - middle_count) // 2
# stop  = start + middle_count
