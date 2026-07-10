# Exercise 3: Find & Replace Tool
# Hardcode a paragraph. Ask user for a word to find and a replacement word.
# Show how many times the word appears, then show the replaced text.


# not using count() insted our own implementation

# using find()
def count_word(string, value):
    start = 0
    count = 0
    while start < len(string):
        index = string.find(value, start)
        if index != -1:
            start = index + len(value)
            count = count + 1
        else:
            return count
    return count


# using split()
# def count_word(string, value):
#     count = 0
#     for word in string.lower().split():
#         word = word.strip(".")
#         if word == value.lower():
#             count = count + 1
#     return count


paragraph = "The cat sat on the mat. The cat was happy. The cat purred."
print(f"Paragraph: {paragraph}")

word_to_find = input("Word to find: ").strip()
word_to_replace_with = input("Replace with: ").strip()

count = count_word(paragraph, word_to_find)
print(f"Ocurrences found: {count}")
print(paragraph.replace(word_to_find, word_to_replace_with))
