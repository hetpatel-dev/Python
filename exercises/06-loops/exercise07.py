# Exercise 7: Word Frequency Counter (Dict Loop)
# Count word frequencies in a sentence using a dict and .items() loop.

sentance = "The, cat. and! the? dog and the bird"
words = sentance.lower().split()

result = dict()

for word in words:
    word = word.strip(",.!?-|'\"")
    if result.get(word):
        result[word] = result[word] + 1
    else:
        result[word] = 1

print(f"Sentance: {sentance}")
for word, count in result.items():
    print(f"{word:<4}: {count:<2}")
