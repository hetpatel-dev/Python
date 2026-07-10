# Index

sentance = "Hello"

print(sentance[0])
print(sentance[1])
print(sentance[2])
print(sentance[3])
print(sentance[4])

print(sentance[-1])
print(sentance[-2])
print(sentance[-3])
print(sentance[-4])
print(sentance[-5])

# is and == both True
print(sentance[0] is sentance[-5])
print(sentance[1] == sentance[-4])
print(sentance[2] == sentance[-3])

# out of bound character access results in IndexError
# print(sentance[100]) # IndexError: string index out of range

# ----------------------------------------------------------------

# Slice: Extract Substring
# [start:stop:step] , start: inclusive | stop: exclusive

print(sentance[:5])  # start: by default 0 or start
print(sentance[0:])  # end: by default len(string) or end

# extracting specific portion
print(sentance[1:4])  # 1, 2, 3 # ell
print(sentance[-4:-1])  # -4, -3, -2 # ell

# step | every second characters
print(sentance[::2])  # 1, 3, 5 # Hlo

# reversing string with slicing
print(sentance[::-1])

# using out of range indexes
print(sentance[0:100])  # Hello

# slicing doesn't throw error for out of bound index access, it automatically adjusts/clamps according to string's length

# ----------------------------------------------------------------

# Immutability

s = "hello"

# can't change characters in place
s[0] = "H"  # TypeError: 'str' object does not support item assignment

# all str operation return a new string than modifying the original

s_upper = s.upper()
print(s)  # hello (unchanged)
print(s_upper)  # HELLO (new str)
print(s is s_upper)  # False , both are different str objects

# When you reassign a variable, you're pointing it at a new string object, not modifying the old one:

name = "Alice"
name = name.upper()  # name points to "ALICE"
# The original "Alice" string still exists but is unreachable.

# Because of immutability, strings are hashable — they can be used as dictionary keys and set elements.

# ----------------------------------------------------------------

# case methods

text = "Hello, World"

print(text.upper())
print(text.lower())
print(text.title())  # each word's first letter uppercase
print(text.capitalize())  # string's first letter uppercase rest lowercase
print(text.swapcase())  # (swap uppercase ↔ lowercase)

# casefold() is more aggressive than lower() — used for caseless matching

german = "Straße"
print(german.lower())  # straße
print(german.casefold())  # strasse

# use cases of each
# - .lower() — general case-insensitive comparison
# - .casefold() — when dealing with non-ASCII text (German ß, Turkish İ, etc.)
# - .title() — formatting names and titles (but watch for edge cases like "O'Brien")
# - .capitalize() — formatting sentences

# ----------------------------------------------------------------

# search and replace methods
# finding characters or substrings within strings

text = "the cat in the hat"

print(text.find("cat"))  # 4 (lowest index value where "cat" starts)
print(text.find("dog"))  # -1 (means not found)
print(text.rfind("the"))  # 11 (lowest index value where "cat" starts)

# .index() is like .find() but raises ValueError on failure
print(text.index("in"))  # 8
# print(text.index("dog"))  # ValueError: substring not found

print((text.count("the")))  # (non-overlapping occurrences)

# Check start and end
print(text.startswith("the"))  # True
print(text.endswith(("the", "hat")))  # True

# Modern Python (3.9+): removeprefix and removesuffix
url = "https://example.com"

print(url.removeprefix("https://"))  # example.com
print(url.removesuffix(".com"))  # https://example

# Replace substrings
print(text.replace("cat", "dog"))  # the dog in the hat
print(text.replace("the", "a"))  # a cat in a hat

# .replace() with count argument:
print(text.replace("the", "A", 1))  # A cat in the hat (only first occurence)

# notes

# search and replace methods

# 1. find(value) -> lowest index index of the value (starts searching from start/left of the string)
# 2. rfind(value) -> highest index of the value in str (starts searching from end/right of the string)
# both return -1 if they can't find value in str

# 3. index(value) -> does same return index of the value
# raise ValError if can't find value

# 4. startswith(value) -> T/F
# 5. endswith(value) -> T/Fs

# 6. removeprefix(prefix) : remove substr from start
# 7. removesufix(sufix) : remove substr from end

# 8. replace(old, new): replace old str with new str
# 9. count(value): number of occurences of given value

# ----------------------------------------------------------------

# split and join

# split: convert string into list of sub strings
# join: convert list of substrings into string

# Split — default splits on any whitespace
sentence = "the quick brown fox"
words = sentence.split()
print(words)

# Split with a specific delimiter
csv_line = "Alice,25,Engineer"
fields = csv_line.split(",")
print(fields)

# Limit splits with maxsplit (for n maxsplit, list items will be n + 1)
data = "one two three four"
print("split 1", data.split(maxsplit=1))  # ['one', 'two three four']
print("split 2", data.split(maxsplit=2))  # ['one', 'two', 'three four']
print("split 3", data.split(maxsplit=3))  # ['one', 'two', 'three', 'four']
print("rsplit 1", data.rsplit(maxsplit=1))  # ['one two three', 'four']
print("rsplit 2", data.rsplit(maxsplit=2))  # ['one two', 'three', 'four']
print("rsplit 3", data.rsplit(maxsplit=3))  # ['one', 'two', 'three', 'four']

# Partition — split at first occurrence, returns 3-tuple
print("a-b-c".partition("-"))  # ('a', '-', 'b-c')
print("a-b-c".rpartition("-"))  # ('a-b', '-', 'c')

# Splitlines — split on newline boundaries
multiline = "line1\nline2\r\nline3"
print(multiline.splitlines())  # ['line1', 'line2', 'line3']

# Join — the inverse of split
result = " | ".join(fields)
print(result)  # Alice | 25 | Engineer

# Join is called ON the separator string, not on the list
parts = ["2026", "07", "08"]
print("-".join(parts))  # 2026-07-08

# Join works with any iterable of strings
print("".join(["a", "b", "c"]))  # abc
# TypeError: sequence item 0: expected str instance, int found
# print("".join([1, 2, 3]))
print("".join(["1", "2", "3"]))  # 123 # convert int -> str

# ----------------------------------------------------------------

# strip and pad

# strip: remove unwanted characters from edge
# pad: add characters to edges to meet the width

# Stripping — default removes whitespace
messy = "  \t  hello   \n"
print(repr(messy.strip()))  # 'hello'
print(repr(messy.lstrip()))  # 'hello   \n'
print(repr(messy.rstrip()))  # '  \t  hello'

# Strip specific characters (not just whitespace)
url = "www.example.com"
print(url.strip("w.com"))  # example

# Padding

print(repr("42".center(10)))  # '    42    '
print(repr("42".ljust(10)))   # '42        '
print(repr("42".rjust(10)))   # '        42'
print(repr("42".zfill(10)))   # '0000000042'
# '-000000042' ( zfill, fills zero and it's sign aware )
print(repr("-42".zfill(10)))

# case methods


def classify(s):
    print(f"{s!r:20} isalpha={s.isalpha():5} isdigit={s.isdigit():5} "
          f"isalnum={s.isalnum():5} isspace={s.isspace():5} "
          f"islower={s.islower():5} isupper={s.isupper():5}")


classify("Hello")   # alpha, not digit, alnum, not space, mixed case
classify("42")      # not alpha, digit, alnum, not space
classify("abc123")  # not pure alpha nor pure digit, but isalnum
classify("   ")     # not alpha, not digit, not alnum, is space
classify("hello")   # all lower
classify("HELLO")   # all upper

# More specialized checks
print("42".isdecimal())    # True  (decimal digits)
print("½".isdecimal())     # False (fraction)
print("½".isnumeric())     # True  (any numeric)
print("Ⅳ".isnumeric())     # True  (Roman numeral)

print(" ".isprintable())   # True  (space is printable)
print("\n".isprintable())  # False (newline is not printable)

print("hello".isidentifier())  # True
print("2cool".isidentifier())  # False (starts with digit)

print("".isascii())        # True  (empty string returns True)
print("café".isascii())    # False (é is non-ASCII)

# ----------------------------------------------------------------

# ord(): convert character to integer code point
# chr(): convert integer code point to character

print(ord("A"))  # 65
print(ord("a"))  # 97
print(ord("0"))  # 48
print(ord("é"))  # 233
print(ord("😊"))  # 128522

print(chr(65))     # A
print(chr(97))     # a
print(chr(128512))  # 😀
